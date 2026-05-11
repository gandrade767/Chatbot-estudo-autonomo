import streamlit as st
import base64


def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
img_base64 = get_image_base64("imgs/pexels-tara-winstead-8386440.jpg")

def mostrar():
    #HTML
    st.markdown(f"""

<h1 class="titulo">Sobre Nós</h1>
<div class="apresentacao">
    <p>Somos quatro mentes, um só propósito: inovar através da tecnologia.
    Transformamos ideias em conversas inteligentes que aproximam pessoas e soluções.
    Nosso projeto nasceu para dar voz à inteligência artificial por meio de um chatbot.</p>
</div>
<div class="imagem">
    <img src="data:image/jpeg;base64,{img_base64}">
</div>
<div class="explicarTabalho">
    <p>Sob a orientação do Professor Andrey, fomos desafiados a explorar as novas fronteiras da inteligência artificial aplicada. Nosso grupo, formado por Adelano Mascarenhas, Antonella Scanoni, Gabriel Andrade e Guilherme Graces, uniu diferentes visões e competências com um propósito comum: transformar tecnologia em diálogo.</p>
    <p>Nosso objetivo principal foi o desenvolvimento de um chatbot inteligente capaz de oferecer uma experiência de conversação fluida e eficiente. Acreditamos que a IA não deve ser apenas uma ferramenta técnica, mas uma ponte que aproxima pessoas de soluções práticas.</p>
    <p>Este projeto reflete nossa dedicação em converter linhas de código em uma interface intuitiva, mostrando como a inovação e o trabalho em equipe podem criar sistemas que realmente entendem e auxiliam o usuário final.</p>
</div>
<div class="conteudoUtilizado">
    <p>Principal Conteúdo Utilizado:</p>
    <div class="links">
        <a href="https://streamlit.io/">-Biblioteca Streamlit</a>
        <p></p>
        <a href="https://huggingface.co/docs/transformers/pt/index">-Biblioteca Transformers</a>
        <p></p>
        <a href="https://numpy.org/">-Biblioteca Numpy</a>
    </div>
    <div class="explicarStreamlit">
        <p>Streamlit: \nFerramenta que transforma código Python em um site interativo, criando a interface e os botões de forma simples.</p>
    </div>
    <div class="explicarTransformers"
        <p>Transformers: \nBiblioteca que fornece os modelos de IA prontos para entender, processar e gerar textos inteligentes.</p>
    </div>
    <div class="explicarNumpy"
        <p>NumPy: \nBiblioteca para manipulação de matrizes e cálculos numéricos de alta performance. É o motor matemático da IA.</p>
    </div>
</div>
""", unsafe_allow_html=True)
    
    
    #CSS

    st.markdown("""
                <style>

                .titulo{
                text-align: center;
                }

                .apresentacao{
                text-align: center;
                margin: 0 auto;
                max-width: 700px;
                margin-top: 30px;
                }
                .imagem img {
                height: 350px;      
                width: 100%;        
                object-fit: cover;  
                object-position: center; 
                border-radius: 10px;
                margin-top:30px;
                }



                .explicarTabalho{
                display:block;
                margin-top:50px;
                text-align:justify;
                float:left;
                width:52%;
                align-content: center;
                border-right: 2px solid white !important;
                }
                .explicarTabalho p{
                display:block;
                margin-right:30px;
                font-size: 20px !important;
                }



                .conteudoUtilizado{
                display:inline-block;
                float:right;
                margin-top:50px;
                text-align:center;
                width:45%;
                font-size: 20px !important;
                }
                .conteudoUtilizado a{
                font-size: 17px !important;
                }
                .conteudoUtilizado{
                font-size: 26px !important;
                }
                .explicarStreamlit{
                width:30%;
                text-align:center;
                display:inline-block;
                margin-top:20px;
                font-size: 17px !important;
                }
                .explicarTransformers{
                width:30%;
                text-align:center;
                display:inline-block;
                margin-top:20px;
                font-size: 17px !important;
                }
                .explicarNumpy{
                width:30%;
                text-align:center;
                display:inline-block;
                margin-top:20px;
                font-size: 17px !important;

                }
                .links a{
                text-decoration:none;
                }

                



                </style>
                """,
                unsafe_allow_html=True)