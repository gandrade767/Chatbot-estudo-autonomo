import streamlit as st
import base64


def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
#IMAGENS UTILIZADAS:
img_base64 = get_image_base64("imgs/pexels-tara-winstead-8386440.jpg")
img_gabriel = get_image_base64("imgs/FotoGabriel.png")
img_gui = get_image_base64("imgs/FotoGui.jpeg")
img_nel = get_image_base64("imgs/FotoAntonella.jpeg")
img_adel = get_image_base64("imgs/FotoAdelano.jpeg")
img_github = get_image_base64("imgs/github-icon-9.png")


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
<div class="criadores">
<h1>Criadores</h1>
</div>
<div class="containerFotos">
    <div class="fotoGabriel">
        <img src="data:image/png;base64,{img_gabriel}">
        <p>Gabriel Andrade</p>
        <a class="linkGithub" href="https://github.com/gandrade767" target="blank"><img class="github" src="data:image/png;base64,{img_github}"></a>
    </div>
    <div class="fotoGui">
        <img src="data:image/jpeg;base64,{img_gui}">
        <p>Guilherme Graces</p>
        <a class="linkGithub" href="https://github.com/GuilhermeGraces" target="blank"><img class="github" src="data:image/png;base64,{img_github}"></a>
    </div>
    <div class="fotoNel">
        <img src="data:image/jpeg;base64,{img_nel}">
        <p>Antonella Scanoni</p>
        <a class="linkGithub" href="https://github.com/Nescauu17" target="blank"><img class="github" src="data:image/png;base64,{img_github}"></a>
    </div>
    <div class="fotoAdel">
        <img src="data:image/jpeg;base64,{img_adel}">
        <p>Adelano Mascarenhas</p>
        <a class="linkGithub" href="https://github.com/Pontas89" target="blank"><img class="github" src="data:image/png;base64,{img_github}"></a>
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
                .explicarStreamlit, .explicarTransformers, .explicarNumpy{
                width:30%;
                text-align:center;
                display:inline-block;
                margin-top:20px;
                font-size: 17px !important;
                }
                
                .links a{
                text-decoration:none;
                display:inline-block;
                transition: transform 0.5s ease-in-out;
                }
                .links a:hover{
                transition: 0.5s;
                transform: scale(1.1);
                color:#B6ECF2 !important;
                }

                
                .criadores{
                clear:both;
                text-align:center;
                margin-top:550px;
                color:#2878d8 !important;
                }
                .containerFotos{
                display:flex;
                clear:both;
                text-align:center;
                }
                .fotoGabriel img, .fotoGui img, .fotoNel img, .fotoAdel img{
                margin-top:100px;
                height:250px;
                width:250px;
                border-radius:100%;
                object-fit: cover;
                }
                .fotoGabriel, .fotoGui, .fotoNel, .fotoAdel{
                width:25%;
                }
                .fotoGabriel p, .fotoGui p, .fotoNel p, .fotoAdel p{
                margin-top:20px;
                font-size: 20px !important;
                margin-bottom: 0px !important;
                }

                .linkGithub{
                display:block
                }

                .github{
                height:70px !important;
                width:70px !important;
                margin-top: 5px !important;
                transition: transform 0.5s ease-in-out;
                }
                .github:hover{
                transition: 0.5s;
                transform: scale(1.1);
                }
                

                </style>
                """,
                unsafe_allow_html=True)