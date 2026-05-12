import streamlit as st
from src.ia_gemini import gerar_resposta_gemini
from src.ia_blenderBot import gerar_resposta_blenderbot
from src.ia_class import gerar_resposta_classificador
import time

def mostrar():
    st.title("Chat")

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

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Pergunte algo..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        historico_para_ia = st.session_state.chat_history.copy()

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                resposta = gerar_resposta_ia(prompt, historico_para_ia)
                st.markdown(resposta)

        st.session_state.chat_history.append({"role": "assistant", "content": resposta})
