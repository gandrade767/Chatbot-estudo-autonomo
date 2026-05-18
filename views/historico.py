import streamlit as st

def mostrar():
    st.markdown("""
        <div style='text-align: center; padding: 10px 0 20px 0;'>
            <h1>Histórico de Conversas</h1>
            <p style='color: gray;'>Veja suas conversas anteriores</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Verifica se a lista de conversas existe e se não está vazia
    if "conversas" not in st.session_state or len(st.session_state.conversas) == 0:
        st.markdown("""
            <div style='text-align: center; padding: 60px 0; color: gray;'>
                <h3>Nenhum chat salvo ainda</h3>
                <p>Inicie uma conversa no Chat Bot e clique em "Salvar Chat" na barra lateral.</p>
            </div>
        """, unsafe_allow_html=True)
        return

    # Itera sobre as conversas salvas e as exibe
    for i, conversa in enumerate(st.session_state.conversas):
        # O título do expander agora usa o "name" e a "data" da conversa
        with st.expander(f"Conversa {i + 1}: {conversa.get('name', 'Chat sem nome')} — {conversa.get('data', 'Data desconhecida')}"):
            # Exibe o modelo usado na conversa
            st.markdown(f"**Modelo:** {conversa.get('model', 'Modelo desconhecido')}")
            st.markdown("---") # Separador visual

            # Itera sobre as mensagens do histórico da conversa
            # Usamos .get('history', []) para evitar erro caso a chave não exista
            for mensagem in conversa.get("history", []):
                with st.chat_message(mensagem["role"]):
                    st.write(mensagem["content"])

            # Botão para continuar a conversa
            # Usamos uma chave única para cada botão (f"continue_chat_{i}")
            if st.button(f"Continuar Conversa {i + 1}", key=f"continue_chat_{i}"):
                # Carrega o histórico da conversa selecionada para o chat_history atual
                st.session_state.chat_history = conversa.get("history", []).copy()
                # Define o modelo selecionado para o modelo da conversa salva
                st.session_state.selected_model = conversa.get("model", "Gemini")
                # Redireciona para a página do chat
                st.session_state.pagina = "chat"
                st.rerun() # Recarrega a página para aplicar as mudanças