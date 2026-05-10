# app.py
import streamlit as st
from views import sobre, chats, chat, inicio

st.set_page_config(
    page_title="Chatbot",
    page_icon="assets/logo.png",
    layout="wide"
)

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicial"

with st.sidebar:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/logo.png", width=60)
    with col2:
        st.markdown("<h2 style='padding-top: 15px;'>Menu</h2>", unsafe_allow_html=True)

    st.divider()

    if st.button("🏠 Página Inicial", use_container_width=True):
        st.session_state.pagina = "inicio"

    if st.button("👾 Chat Bot", use_container_width=True):
        st.session_state.pagina = "chat"

    if st.button("💬 Histórico de Chats", use_container_width=True):
        st.session_state.pagina = "chats"

    if st.button("🏢 Sobre Nós", use_container_width=True):
        st.session_state.pagina = "sobre"

    st.divider()
    st.caption("v1.0.0")

if st.session_state.pagina == "inicio":
    inicio.mostrar()
elif st.session_state.pagina == "chat":
    chat.mostrar()
elif st.session_state.pagina == "chats":
    chats.mostrar()
elif st.session_state.pagina == "sobre":
    sobre.mostrar()
else:
    inicio.mostrar()