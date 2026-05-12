import streamlit as st

def mostrar():
    st.markdown("""
        <div style='text-align: center; padding: 10px 0 20px 0;'>
            <h1>Histórico de ConversasS</h1>
            <p style='color: gray;'>Veja suas conversas anteriores</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    if "conversas" not in st.session_state or len(st.session_state.conversas) == 0:
        st.markdown("""
            <div style='text-align: center; padding: 60px 0; color: gray;'>
                <h3>Nenhum chat salvo ainda</h3>
                <p>Inicie uma conversa no Chat Bot</p>
            </div>
        """, unsafe_allow_html=True)
        return

    for i, conversa in enumerate(st.session_state.conversas):
        with st.expander(f"Conversa {i + 1} — {conversa['data']}"):
            for mensagem in conversa["historico"]:
                with st.chat_message(mensagem["role"]):
                    st.write(mensagem["content"])