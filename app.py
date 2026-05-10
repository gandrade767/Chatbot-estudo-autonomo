# app.py
import streamlit as st
from src.ia import gerar_resposta
from views import sobre, chats, chat, inicio

# Config da pagina nome e logo
st.set_page_config(
    page_title="Chatbot",
    page_icon="assets/logo.png",
    layout="wide"
)

# Set paginal inicial
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicial"

# Sidebar
with st.sidebar:
    st.image("assets/logo.png", width=80)
    st.title("Menu")
    st.divider()

    if st.button("Pagina Inicial", use_container_width=True):
        st.session_state.pagina = "inicio"

    if st.button("Chat Bot", use_container_width=True):
        st.session_state.pagina = "chat"

    if st.button("Chats abertos", use_container_width=True):
        st.session_state.pagina = "chats"

    if st.button("Sobre Nós", use_container_width=True):
        st.session_state.pagina = "sobre"

    st.divider()
    st.caption("v1.0.0")

if st.session_state.pagina == "inicio":
    inicio.mostrar()

if st.session_state.pagina == "sobre":
    sobre.mostrar()

elif st.session_state.pagina == "chat":
    st.title("Chatbot")

    if "historico" not in st.session_state:
        st.session_state.historico = []

    for mensagem in st.session_state.historico:
        with st.chat_message(mensagem["role"]):
            st.write(mensagem["content"])

    pergunta = st.chat_input("Digite sua mensagem...")

    if pergunta:
        with st.chat_message("user"):
            st.write(pergunta)

        st.session_state.historico.append({"role": "user", "content": pergunta})

        resposta = gerar_resposta(pergunta)

        with st.chat_message("assistant"):
            st.write(resposta)

        st.session_state.historico.append({"role": "assistant", "content": resposta})

else:
    st.title("Bem vindo ao Chatbot!")