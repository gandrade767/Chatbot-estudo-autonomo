import streamlit as st
from views import sobre, chats, chat, inicio
import base64

# Função para converter imagem para base64
def get_img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Configurações iniciais da página do Streamlit
st.set_page_config(
    page_title="Chatbot",
    page_icon="assets/logo.png",
    layout="wide"
)

# Carrega o logo em base64 para uso no HTML/CSS
logo_b64 = get_img_base64("assets/logo.png")

#Este bloco injeta CSS na página para estilizar a barra lateral e os botões.
st.markdown(f"""
    <style>
        [data-testid="stSidebar"] {{
            background-color: #1a1a2e;
        }}

        [data-testid="stSidebarContent"] {{
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }}

        [data-testid="stSidebar"] .stButton > button {{
            background-color: transparent;
            color: #e0e0e0;
            border: 1px solid #ffffff15;
            border-radius: 10px;
            padding: 10px 16px;
            text-align: center;
            transition: all 0.3s ease;
            font-size: 14px;
            font-weight: 400;
            letter-spacing: 0.3px;
        }}

        [data-testid="stSidebar"] .stButton > button:hover {{
            background-color: #ffffff10;
            border-color: #ffffff30;
            color: white;
        }}

        .sidebar-header {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 28px 0 12px 0;
            width: 100%;
        }}

        .sidebar-header img {{
            border-radius: 16px;
            width: 72px;
            height: 72px;
            object-fit: contain;
        }}

        .sidebar-header h1 {{
            color: white;
            font-size: 17px;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin: 10px 0 2px 0;
            text-align: center;
        }}

        .sidebar-header p {{
            color: #7a7a9a;
            font-size: 12px;
            margin: 0;
            text-align: center;
        }}

        .sidebar-spacer {{
            flex-grow: 1;
        }}

        .sidebar-footer {{
            text-align: center;
            color: #3a3a5a;
            font-size: 11px;
            padding: 16px 0 20px 0;
            width: 100%;
        }}

        /* Estilo para os botões de navegação personalizados */
        .nav-btn {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 11px 16px;
            margin-bottom: 6px;
            background-color: transparent;
            color: #c0c0d0;
            border: 1px solid #ffffff15;
            border-radius: 10px;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s ease;
            box-sizing: border-box;
        }}

        .nav-btn:hover {{
            background-color: #ffffff10;
            border-color: #ffffff30;
            color: white;
        }}

        .nav-btn svg {{
            width: 16px;
            height: 16px;
            stroke: currentColor;
            flex-shrink: 0;
        }}
    </style>

    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
""", unsafe_allow_html=True)

#Estas funções garantem que certas variáveis existam no estado da sessão do Streamlit.
def inicializar_estado_sessao():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "Gemini" # Modelo padrão
    if "loading" not in st.session_state:
        st.session_state.loading = False
    if "chat_active" not in st.session_state:
        st.session_state.chat_active = False
    if "current_chat" not in st.session_state:
        st.session_state.current_chat = None
    if "saved_chats" not in st.session_state:
        st.session_state.saved_chats = []
    if "pagina" not in st.session_state: # Garante que a página inicial seja definida
        st.session_state.pagina = "inicio"

# Chama a função para garantir que o estado da sessão esteja configurado
inicializar_estado_sessao()

# Sidebar
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

    if st.button("⌂  Página Inicial", use_container_width=True, key="nav_inicio"):
        st.session_state.pagina = "inicio"

    if st.button(" (☞ﾟヮﾟ)☞ Chat Bot", use_container_width=True, key="nav_chat"):
        st.session_state.pagina = "chat"

    if st.button("↺  Histórico de Chats", use_container_width=True, key="nav_chats"):
        st.session_state.pagina = "chats"

    if st.button("ℹ  Sobre Nós", use_container_width=True, key="nav_sobre"):
        st.session_state.pagina = "sobre"

    #Seletor de Modelo de IA
    if st.session_state.pagina == "chat":
        st.markdown("---")
        st.session_state.selected_model = st.selectbox(
            "Selecione o Modelo de IA:",
            ("Gemini", "BlenderBot", "Classificador"),
            index=["Gemini", "BlenderBot", "Classificador"].index(st.session_state.selected_model) if st.session_state.selected_model in ["Gemini", "BlenderBot", "Classificador"] else 0,
            key="model_selector"
        )
        # Botões de Limpar e Salvar Chat (movidos para a barra lateral, visíveis na página de Chat)
        if st.button("Limpar Chat", key="clear_chat_button", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.current_chat = None
            st.session_state.chat_active = False
            st.rerun()

        if st.button("Salvar Chat", key="save_chat_button", use_container_width=True):
            if st.session_state.chat_history:
                chat_name = st.session_state.chat_history[0]["content"][:30] + "..." if st.session_state.chat_history[0]["role"] == "user" else "Novo Chat"
                st.session_state.saved_chats.append({
                    "name": chat_name,
                    "history": st.session_state.chat_history.copy(),
                    "model": st.session_state.selected_model
                })
                st.success(f"Chat '{chat_name}' salvo!")
            else:
                st.warning("Não há chat para salvar.")


    st.markdown("<div class='sidebar-spacer'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-footer'>v1.0.0 · Chatbot</div>", unsafe_allow_html=True)

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