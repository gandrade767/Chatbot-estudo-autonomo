# views/chat.py
import streamlit as st
from src.ia import gerar_resposta
from datetime import datetime

def mostrar():
    st.markdown("""
        <div style='text-align: center; padding: 10px 0 20px 0;'>
            <h1>Chatbot</h1>
            <p style='color: gray;'>Tire suas dúvidas com a IA</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    if "historico" not in st.session_state:
        st.session_state.historico = []

    if "conversas" not in st.session_state:
        st.session_state.conversas = []

    if len(st.session_state.historico) > 0:
        if st.button("Encerrar e salvar conversa"):
            st.session_state.conversas.append({
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "historico": st.session_state.historico.copy()
            })
            st.session_state.historico = []
            st.success("Conversa salva!")
            st.rerun()

    if len(st.session_state.historico) == 0:
        st.markdown("""
            <div style='text-align: center; padding: 60px 0; color: gray;'>
                <h3>Nenhuma mensagem ainda</h3>
                <p>Comece digitando sua pergunta abaixo 👇</p>
            </div>
        """, unsafe_allow_html=True)

    for mensagem in st.session_state.historico:
        with st.chat_message(mensagem["role"]):
            st.write(mensagem["content"])

    pergunta = st.chat_input("Digite sua mensagem...")

    if pergunta:
        with st.chat_message("user"):
            st.write(pergunta)
        st.session_state.historico.append({"role": "user", "content": pergunta})

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                resposta = gerar_resposta(pergunta)
            st.write(resposta)

        st.session_state.historico.append({"role": "assistant", "content": resposta})