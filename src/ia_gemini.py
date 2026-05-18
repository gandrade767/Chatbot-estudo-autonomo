import streamlit as st
import google.generativeai as genai
 # Importe se for usar safety_settings
from google.generativeai.types import HarmCategory, HarmBlockThreshold

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
        - Secretaria: funciona de segunda a sexta das 07:00h às 22:00h | Fale conosco https://www.unigran.br/campogrande/fale-conosco
        - Coordenação: envie e-mail ou vá ao bloco X
        - Notas: acesse o portal do aluno em https://area.campogrande.unigran.br
        - Dúvidas gerais sobre a vida acadêmica

        Se não souber a resposta, oriente o aluno a procurar a secretaria.
        Seja simpático e acolhedor, lembrando que são calouros.
        """,
        # Configurações de segurança
        safety_settings=SAFETY_SETTINGS 
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

    # Remove a última mensagem (pergunta do usuário)
    historico_para_start_chat = gemini_historico[:-1]

    chat = model.start_chat(history=historico_para_start_chat)

    # A pergunta atual é enviada aqui
    response = chat.send_message(pergunta)

    return response.text
