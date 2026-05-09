import streamlit as st
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from deep_translator import GoogleTranslator

# carregando o modelo
@st.cache_resource
def carregar_modelo():
    modelo = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(modelo)
    model = BlenderbotForConditionalGeneration.from_pretrained(modelo)
    return tokenizer, model

tokenizer, model = carregar_modelo()

#   página inicial

def inicial():
    st.title("fodase")
    return


#   criando uma sidebar

with st.sidebar:

    st.title("🚀 Menu")

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

    # exibindo o histórico
    for mensagem in st.session_state.historico:
        with st.chat_message(mensagem["role"]):
            st.write(mensagem["content"])

    # input do usuário
    pergunta = st.chat_input("Digite sua mensagem...")

    if pergunta:
        with st.chat_message("user"):
            st.write(pergunta)

        st.session_state.historico.append({"role": "user", "content": pergunta})

        # traduz pergunta para inglês
        pergunta_en = GoogleTranslator(source="pt", target="en").translate(pergunta)

        # tokeniza e gera resposta
        inputs = tokenizer(pergunta_en, return_tensors="pt")
        output = model.generate(**inputs, max_new_tokens=100)
        resposta_en = tokenizer.decode(output[0], skip_special_tokens=True)

        # traduz resposta para português
        resposta = GoogleTranslator(source="en", target="pt").translate(resposta_en)

        with st.chat_message("assistant"):
            st.write(resposta)

        st.session_state.historico.append({"role": "assistant", "content": resposta})