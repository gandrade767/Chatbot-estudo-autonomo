# views/inicio.py
import streamlit as st

def mostrar():
    st.markdown("""
        <div style='text-align: center; padding: 20px 0 40px 0;'>
            <h1>🤖 Bem-vindo ao Seu Assistente de IA!</h1>
            <p style='font-size: 1.2em; color: #c0c0d0;'>
                Explore o poder da inteligência artificial em suas conversas.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Seção de Destaque de Funcionalidades
    st.markdown("""
        <div style='padding: 20px;'>
            <h2 style='text-align: center;'>O que você pode fazer aqui?</h2>
            <ul style='font-size: 1.1em; line-height: 1.8;'>
                <li>Converse com diferentes modelos de IA, como <strong>Gemini</strong>, <strong>BlenderBot</strong> e um <strong>Classificador</strong>.</li>
                <li>Salve suas conversas importantes para revisitar a qualquer momento.</li>
                <li>Continue uma conversa salva do seu histórico.</li>
                <li>Desfrute de uma experiência otimizada com gerenciamento inteligente de contexto.</li>
            </ul>
            <p style='text-align: center; font-size: 1.1em; margin-top: 30px;'>
                Use a barra lateral à esquerda para navegar e começar sua jornada!
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Chamada para Ação
    col1, col2, col3 = st.columns([1, 2, 1]) # Centraliza o botão
    with col2:
        if st.button("Iniciar um Novo Chat", use_container_width=True):
            st.session_state.pagina = "chat" # Muda para a página do chat
            st.rerun() # Recarrega o Streamlit para mostrar a nova página

    st.markdown("---")

    st.info("Dica: Experimente diferentes modelos de IA para ver suas capacidades únicas e encontre o que melhor se adapta às suas necessidades!")
