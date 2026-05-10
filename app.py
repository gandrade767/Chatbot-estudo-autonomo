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

#   página inicial

def inicial():
    st.title("fodase")
    return


#   criando uma sidebar

with st.sidebar:
    st.image("assets/logo.png", width=80)
    st.title("Menu")
    st.divider()

    pagSobre= st.button("🏢 Sobre Nós", use_container_width=True)
    

    st.write("")

    pagChat= st.button("👾 Chat Bot", use_container_width=True)
    

#   pagina Sobre nós

if pagSobre:
    st.title("oioi")


# pagina do chatbot

elif pagChat:

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