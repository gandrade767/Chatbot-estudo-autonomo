import streamlit as st
from views import historico, sobre, chat, inicio
from src.components.sidebar import mostrar_sidebar # Importa a nova função da sidebar
# Remova a importação de base64 e datetime daqui, pois já estão na sidebar.py se não forem usadas em outro lugar no app.py

# As configurações de CSS para a sidebar também podem ser movidas para a sidebar.py
# ou mantidas aqui se afetarem outros elementos globais.
# Por simplicidade, vou manter o CSS aqui por enquanto, mas ele pode ser refatorado.
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1a1a2e;
        }

        [data-testid="stSidebarContent"] {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }

        [data-testid="stSidebar"] .stButton > button {
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
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            background-color: #ffffff10;
            border-color: #ffffff30;
            color: white;
        }

        .sidebar-header {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 28px 0 12px 0;
            width: 100%;
        }

        .sidebar-header img {
            border-radius: 16px;
            width: 72px;
            height: 72px;
            object-fit: contain;
        }

        .sidebar-header h1 {
            color: white;
            font-size: 17px;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin: 10px 0 2px 0;
            text-align: center;
        }

        .sidebar-header p {
            color: #7a7a9a;
            font-size: 12px;
            margin: 0;
            text-align: center;
        }

        .sidebar-spacer {
            flex-grow: 1;
        }

        .sidebar-footer {
            text-align: center;
            color: #3a3a5a;
            font-size: 11px;
            padding: 16px 0 20px 0;
            width: 100%;
        }

        /* Estilo para os botões de navegação personalizados */
        .nav-btn {
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
        }

        .nav-btn:hover {
            background-color: #ffffff10;
            border-color: #ffffff30;
            color: white;
        }

        .nav-btn svg {
            width: 16px;
            height: 16px;
            stroke: currentColor;
            flex-shrink: 0;
        }
    </style>

    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
""", unsafe_allow_html=True)


# Configurações iniciais da página do Streamlit
st.set_page_config(
    page_title="Chatbot",
    page_icon="assets/logo.png",
    layout="wide"
)

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
    if "conversas" not in st.session_state:
        st.session_state.conversas = []
    if "pagina" not in st.session_state: # Garante que a página inicial seja definida
        st.session_state.pagina = "inicio"

# Chama a função para garantir que o estado da sessão esteja configurado
inicializar_estado_sessao()

# Chama a função que renderiza a sidebar
mostrar_sidebar()

# Lógica de roteamento das páginas
if st.session_state.pagina == "inicio":
    inicio.mostrar()
elif st.session_state.pagina == "chat":
    chat.mostrar()
elif st.session_state.pagina == "historico":
    historico.mostrar()
elif st.session_state.pagina == "sobre":
    sobre.mostrar()
else:
    inicio.mostrar()