import streamlit as st
from transformers import pipeline

@st.cache_resource
def carregar_modelo_classificador():
    """
    Carrega o modelo de classificação de texto (BART Large MNLI)
    para identificar a intenção da pergunta do usuário.
    """
    # device=-1 significa usar CPU. Se tiver GPU e quiser usar, mude para device=0
    pipe = pipeline(model="facebook/bart-large-mnli", device=-1)
    return pipe

def gerar_resposta_classificador(pergunta: str, historico: list) -> str:
    """
    Gera uma resposta baseada na classificação da pergunta do usuário.

    Args:
        pergunta (str): A pergunta do usuário.
        historico (list): O histórico da conversa (não usado diretamente por este modelo,
                          mas mantido para compatibilidade de assinatura).

    Returns:
        str: A resposta gerada pelo classificador.
    """
    pipe = carregar_modelo_classificador()

    # Categorias que o modelo tentará identificar na pergunta do usuário
    candidate_labels = ["Matricula", "secretaria", "coordenação", "notas"]

    # Realiza a classificação da pergunta
    resultado = pipe(pergunta, candidate_labels=candidate_labels)
    # Pega a categoria com maior score
    categoria = resultado["labels"][0]
    # Pega o score de confiança
    score = resultado["scores"][0]

    # Respostas pré-definidas para cada categoria
    respostas_pre_definidas = {
        "notas": "Para ver suas notas acesse o portal do aluno.",
        "Matricula": "Para matrícula procure a secretaria no bloco X.",
        "secretaria": "A secretaria funciona de segunda a sexta das 8h às 18h.",
        "coordenação": "Para falar com a coordenação, envie um e-mail ou vá ao bloco X.",
    }

    # Obtém a resposta baseada na categoria, ou uma mensagem padrão se não entender
    resposta = respostas_pre_definidas.get(categoria, "Não entendi, pode reformular?")

    # Adiciona a confiança da classificação à resposta
    return f"{resposta}"
