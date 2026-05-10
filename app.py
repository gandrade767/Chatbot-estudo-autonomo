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
#a criar


#   criando uma sidebar
if "pagina" not in st.session_state:
    st.session_state.pagina = "chat"

with st.sidebar:

    st.title("🚀 Menu")

    st.divider()

    if st.button("🏢 Sobre Nós", use_container_width=True):
        st.session_state.pagina = "sobre"
    

    st.write("")

    if st.button("👾 Chat Bot", use_container_width=True):
        st.session_state.pagina = "chat"
    

#   pagina Sobre nós

if st.session_state.pagina =="sobre":
    st.title("Sobre nós")
    st.divider()
    st.image("imgs/imagemSobreNos.jpg")
    st.divider()
    st.markdown("Somos uma equipe apaixonada por tecnologia, inovação e pelo impacto que a inteligência artificial pode causar na vida das pessoas. Formado por Gabriel Andrade, Guilherme Graces, Antonella Scanoni e Adelano Mascarenhas, nosso grupo desenvolveu um projeto com o objetivo de aproximar a tecnologia das pessoas de forma prática, inteligente e acessível. \n Nosso foco é a criação de um agente de inteligência artificial capaz de conversar de maneira eficiente, natural e dinâmica, oferecendo respostas rápidas, úteis e humanizadas. Mais do que apenas responder perguntas, buscamos construir uma experiência interativa que facilite a comunicação e torne o uso da tecnologia algo simples e agradável para todos. \n Acreditamos que a IA tem o poder de transformar a forma como as pessoas aprendem, trabalham e se conectam. Por isso, unimos criatividade, dedicação e conhecimento para desenvolver uma solução moderna, funcional e preparada para evoluir constantemente junto às necessidades dos usuários. \n Este projeto representa não apenas nosso interesse pela área da tecnologia, mas também nosso compromisso em criar algo inovador, útil e capaz de gerar impacto positivo no cotidiano das pessoas.")


# pagina do chatbot

elif st.session_state.pagina =="chat":

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