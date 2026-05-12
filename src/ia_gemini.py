import streamlit as st
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold # Importe se for usar safety_settings

@st.cache_resource
def carregar_modelo_gemini():
    # Verificação se API key ta config
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("Chave GEMINI_API_KEY não encontrada em .streamlit/secrets.toml")
        st.stop()

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    # Configurações de segurança (opcional, mas bom ter)
    SAFETY_SETTINGS = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction="""
        Você é um assistente virtual para calouros da faculdade.
        Responda sempre em português de forma clara e objetiva.
        Você pode ajudar com informações sobre:
        - Matrícula: procure a secretaria no bloco X
        - Secretaria: funciona de segunda a sexta das 8h às 18h
        - Coordenação: envie e-mail ou vá ao bloco X
        - Notas: acesse o portal do aluno em portal.faculdade.com.br
        - Dúvidas gerais sobre a vida acadêmica

        Se não souber a resposta, oriente o aluno a procurar a secretaria.
        Seja simpático e acolhedor, lembrando que são calouros.
        """,
        safety_settings=SAFETY_SETTINGS # Adicione as configurações de segurança
    )
    return model

def gerar_resposta_gemini(pergunta: str, historico: list) -> str:
    model = carregar_modelo_gemini()

    # Converte o histórico do Streamlit (lista de dicts {"role": "...", "content": "..."})
    # para o formato esperado pelo Gemini (lista de dicts {"role": "...", "parts": [{"text": "..."}]})
    gemini_historico = []
    for msg in historico:
        # O Gemini usa 'user' e 'model' como roles
        role = "user" if msg["role"] == "user" else "model"
        # Cada item em 'parts' deve ser um dicionário com a chave 'text'
        gemini_historico.append({"role": role, "parts": [{"text": msg["content"]}]})

    # Inicia um chat com o histórico formatado
    # Importante: o Gemini espera que o histórico termine com uma resposta do 'model'.
    # Se a última mensagem no 'historico' do Streamlit for do 'user',
    # e você passar para o Gemini, ele pode dar erro.
    # A API do Gemini lida com isso se você passar o histórico e a pergunta separadamente.
    # O 'historico' que vem do Streamlit já inclui a última pergunta do usuário.
    # Portanto, o 'historico' que você passa para o start_chat deve ser o histórico
    # ANTES da pergunta atual do usuário.
    # No views/chat.py, você passa `historico_para_ia` que é uma cópia do `st.session_state.chat_history`.
    # O `st.session_state.chat_history` já tem a pergunta atual do usuário.
    # A API do Gemini espera que o `history` do `start_chat` contenha apenas os turnos ANTERIORES.
    # A pergunta atual é passada no `send_message`.

    # Para evitar o erro, vamos remover a última mensagem (que é a pergunta atual do usuário)
    # do histórico que passamos para start_chat, e a passaremos separadamente em send_message.
    # Isso é crucial para o Gemini API.
    historico_para_start_chat = gemini_historico[:-1] # Remove a última mensagem (pergunta do usuário)

    chat = model.start_chat(history=historico_para_start_chat)
    response = chat.send_message(pergunta) # A pergunta atual é enviada aqui

    return response.text
