# Chatbot em Português 🤖

Chatbot conversacional em português utilizando o modelo BlenderBot da Meta com tradução automática via Google Translator.

## Tecnologias utilizadas

- Python
- Streamlit
- Transformers (Hugging Face)
- Deep Translator
- PyTorch

## Pré-requisitos

- Python 3.10 ou superior
- Git

## Como rodar o projeto

### 1. Clone o repositório

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

### 2. Crie o ambiente virtual

python -m venv venv

### 3. Ative o ambiente virtual

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

### 4. Instale as dependências

pip install -r requirements.txt

### 5. Rode a aplicação

streamlit run app.py

## Como funciona

O chatbot recebe a mensagem do usuário em português, traduz para inglês, processa com o modelo BlenderBot e traduz a resposta de volta para português.

## Observações

- Na primeira execução o modelo será baixado automaticamente (cerca de 1.7GB)
- Recomendado ter pelo menos 8GB de RAM