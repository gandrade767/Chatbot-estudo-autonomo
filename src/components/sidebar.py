# src/components/sidebar.py
import streamlit as st
import base64
from datetime import datetime # Necessário para o timestamp do chat salvo

# Função para converter imagem para base64 (pode ser movida para um utilitário se usada em mais lugares)
def get_img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def mostrar_sidebar():
    # Carrega o logo em base64 para uso no HTML/CSS
    logo_b64 = get_img_base64("assets/logo.png") # Certifique-se de que o caminho para 'assets/logo.png' está correto a partir da raiz do projeto

    with st.sidebar:
        # Cabeçalho da barra lateral com logo e titulo
        st.markdown(f"""
            <div class='sidebar-header'>
                <img src='data:image/png;base64,{logo_b64}'/>
                <h1>Chatbot</h1>
                <p>Assistente</p>
            </div>
        """, unsafe_allow_html=True)

        st.divider()

        # Botões de navegação
        if st.button("⌂  Página Inicial", use_container_width=True, key="nav_inicio"):
            st.session_state.pagina = "inicio"

        if st.button("☞ Chat Bot", use_container_width=True, key="nav_chat"):
            st.session_state.pagina = "chat"

        if st.button("↺  Histórico de Chats", use_container_width=True, key="nav_historico"):
            st.session_state.pagina = "historico"

        if st.button("ℹ  Sobre Nós", use_container_width=True, key="nav_sobre"):
            st.session_state.pagina = "sobre"

        # Seletor de Modelo de IA e botões de ação (visíveis apenas na página de Chat)
        if st.session_state.pagina == "chat":
            st.markdown("---")
            st.session_state.selected_model = st.selectbox(
                "Selecione o Modelo de IA:",
                ("Gemini", "BlenderBot", "Classificador"),
                index=["Gemini", "BlenderBot", "Classificador"].index(st.session_state.selected_model) if st.session_state.selected_model in ["Gemini", "BlenderBot", "Classificador"] else 0,
                key="model_selector"
            )

            if st.button("Limpar Chat", key="clear_chat_button", use_container_width=True):
                st.session_state.chat_history = []
                st.session_state.current_chat = None
                st.session_state.chat_active = False
                st.rerun()

            if st.button("Salvar Chat", key="save_chat_button", use_container_width=True):
                if st.session_state.chat_history:
                    chat_name = st.session_state.chat_history[0]["content"][:30] + "..." if st.session_state.chat_history and st.session_state.chat_history[0]["role"] == "user" else "Novo Chat"

                    st.session_state.conversas.append({
                        "name": chat_name,
                        "history": st.session_state.chat_history.copy(),
                        "model": st.session_state.selected_model,
                        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    })
                    st.success(f"Chat '{chat_name}' salvo!")
                else:
                    st.warning("Não há chat para salvar.")

        st.markdown("<div class='sidebar-spacer'></div>", unsafe_allow_html=True)
        st.markdown("<div class='sidebar-footer'>v1.0.0 · Chatbot</div>", unsafe_allow_html=True)