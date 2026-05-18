import streamlit as st
from src.ia_gemini import gerar_resposta_gemini
from src.ia_blenderBot import gerar_resposta_blenderbot
from src.ia_class import gerar_resposta_classificador
import time
from src.gerenciador_historico import ( # Importa as novas funções
    inicializar_historico,
    adicionar_mensagem,
    obter_historico_para_ia,
    pre_processar_prompt
)

def mostrar():
    st.title("Chat")

    # Inicializa o histórico da conversa atual se ainda não foi inicializado
    inicializar_historico()

    # A lista de conversas salvas ("conversas") é inicializada em app.py
    # e o botão de salvar também está em app.py, então não precisamos mexer aqui.

    #Seleção da Função de IA
    if st.session_state.selected_model == "Gemini":
        gerar_resposta_ia = gerar_resposta_gemini
    elif st.session_state.selected_model == "BlenderBot":
        gerar_resposta_ia = gerar_resposta_blenderbot
    elif st.session_state.selected_model == "Classificador":
        gerar_resposta_ia = gerar_resposta_classificador
    else:
        st.error("Modelo de IA não selecionado ou inválido.")
        return

    # Exibe o histórico da conversa atual
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Pergunte algo..."):
        # Pré-processa o prompt do usuário para limpar espaços
        processed_prompt = pre_processar_prompt(prompt)

        # Adiciona o prompt processado ao histórico
        adicionar_mensagem("user", processed_prompt)
        with st.chat_message("user"):
            st.markdown(processed_prompt) # Exibe o prompt já limpo

        # Obtém o histórico limitado para enviar à IA
        historico_para_ia = obter_historico_para_ia()

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                # Envia o prompt processado e o histórico limitado para a IA
                resposta = gerar_resposta_ia(processed_prompt, historico_para_ia)
                st.markdown(resposta)

        # Adiciona a resposta da IA ao histórico
        adicionar_mensagem("assistant", resposta)
