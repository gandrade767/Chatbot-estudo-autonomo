# Chatbot Inteligente com Múltiplos Modelos de IA

Este projeto apresenta um chatbot interativo construído com Streamlit, capaz de se comunicar utilizando diferentes modelos de Inteligência Artificial, como Google Gemini, BlenderBot e um Classificador de Texto. Ele oferece uma experiência de usuário rica com histórico de conversas, gerenciamento de contexto e uma interface intuitiva.

## Funcionalidades Principais

*   **Múltiplos Modelos de IA:** Alterne entre diferentes modelos de IA para diversas necessidades:
    *   **Google Gemini:** Para conversas dinâmicas e geração de texto avançada.
    *   **BlenderBot:** Um modelo de conversação mais geral.
    *   **Classificador de Texto:** Para categorizar ou analisar textos (funcionalidade específica a ser detalhada).
*   **Histórico de Conversas:** Todas as suas interações são salvas, permitindo que você revisite e continue conversas anteriores.
*   **Gerenciamento de Contexto:** Otimização inteligente do histórico da conversa para manter o contexto relevante sem exceder limites de tokens.
*   **Interface Intuitiva:** Desenvolvido com Streamlit para uma experiência de usuário fluida e responsiva.
*   **Modularidade:** Código organizado em componentes para facilitar a manutenção e escalabilidade.

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o chatbot em sua máquina local.

### Pré-requisitos

*   Python 3.9+
*   `pip` (gerenciador de pacotes do Python)

### 1. Clonar o Repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd Chatbot-estudo-autonomo # Ou o nome da pasta do seu projeto
```
**Nota:** Substitua `<URL_DO_SEU_REPOSITORIO>` pela URL real do seu repositório Git.

### 2. Criar e Ativar o Ambiente Virtual

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

```bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
```

### 3. Instalar as Dependências

Instale todas as bibliotecas necessárias a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar Segredos (Chaves de API)

Este projeto utiliza chaves de API para acessar modelos de IA (como o Google Gemini). O Streamlit gerencia segredos de forma nativa através do arquivo `.streamlit/secrets.toml`.

1.  **Crie a pasta `.streamlit`** na raiz do seu projeto, se ela ainda não existir.
2.  **Crie um arquivo `secrets.toml`** dentro da pasta `.streamlit`.
3.  **Adicione suas chaves de API** no formato TOML dentro de `.streamlit/secrets.toml`:

    ```toml
    # .streamlit/secrets.toml
    GOOGLE_API_KEY="SUA_CHAVE_API_DO_GOOGLE_GEMINI"
    ```
    **Importante:** Nunca compartilhe seu arquivo `secrets.toml` ou suas chaves de API publicamente. Adicione `.streamlit/secrets.toml` ao seu `.gitignore`.

4.  **Acesso no Código:** No seu código Streamlit, você pode acessar a chave da seguinte forma:
    ```python
    import streamlit as st
    api_key = st.secrets["GOOGLE_API_KEY"]
    ```

### 5. Executar o Chatbot

Com o ambiente virtual ativado e as dependências instaladas, você pode iniciar o aplicativo Streamlit:

```bash
streamlit run app.py
```

O chatbot será aberto automaticamente no seu navegador padrão.

## Estrutura do Projeto
## Estrutura de Pastas

```text
meu-projeto-streamlit/
├── .github/              # Se houver fluxos de automação (ex: CI/CD)
├── .streamlit/           # Configurações e segredos do Streamlit
│   └── secrets.toml      # Armazena chaves de API e outros segredos
├── imgs/                 # Pasta para imagens e assets
│   └── pexels-tara-winstead-8386411.jpg
├── src/                  # Código fonte principal
│   ├── __init__.py
│   ├── components/       # Componentes reutilizáveis da UI
│   │   └── sidebar.py    # Lógica e layout da barra lateral
│   └── utils/            # Funções utilitárias
│       ├── chat_history.py
│       └── token_manager.py
├── venv/                 # Ambiente virtual (ignorado pelo Git)
├── views/                # Páginas/Telas do aplicativo
│   ├── __init__.py
│   ├── chat.py           # Tela principal do chatbot
│   ├── historico.py      # Tela para gerenciar o histórico
│   └── inicio.py         # Tela inicial de boas-vindas
├── .gitignore            # Arquivos e pastas ignorados pelo Git
├── app.py                # Ponto de entrada principal do Streamlit
├── README.md             # Este arquivo de documentação
└── requirements.txt      # Dependências do projeto (pip)
```


## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma issue ou enviar um Pull Request.