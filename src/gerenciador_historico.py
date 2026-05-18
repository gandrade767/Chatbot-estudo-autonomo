import streamlit as st
LIMITE_HISTORICO = 6 # mantém as últimas 6 mensagens (3 do usuário e 3 do assistente)

def inicializar_historico():
    """Inicializa o chat_history na session_state se ainda não existir."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def adicionar_mensagem(role: str, content: str):
    """Adiciona uma mensagem ao histórico da conversa atual."""
    inicializar_historico()
    st.session_state.chat_history.append({"role": role, "content": content})

def obter_historico_para_ia() -> list:
    """
    Retorna uma cópia do histórico da conversa atual, limitado ao LIMITE_HISTORICO,
    para ser enviado à IA.
    """
    inicializar_historico()
    # Retorna as mensagens mais recentes, limitadas pelo LIMITE_HISTORICO
    return st.session_state.chat_history[-LIMITE_HISTORICO:].copy()

def limpar_historico_completo():
    """Limpa todo o histórico da conversa atual."""
    st.session_state.chat_history = []

def pre_processar_prompt(prompt: str) -> str:
    """
    Realiza o pré-processamento do prompt do usuário para otimização de tokens.
    - Remove espaços em branco do início e fim.
    - Substitui múltiplos espaços por um único espaço.
    """
    processed_prompt = prompt.strip()
    processed_prompt = ' '.join(processed_prompt.split())
    return processed_prompt
