# src/ia.py
import streamlit as st
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from src.utils.utils import traduzir

@st.cache_resource
def carregar_modelo():
    modelo = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(modelo)
    model = BlenderbotForConditionalGeneration.from_pretrained(modelo)
    return tokenizer, model

def gerar_resposta(pergunta: str) -> str:
    tokenizer, model = carregar_modelo()
    pergunta_en = traduzir(pergunta, "pt", "en")
    inputs = tokenizer(pergunta_en, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=100)
    resposta_en = tokenizer.decode(output[0], skip_special_tokens=True)
    return traduzir(resposta_en, "en", "pt")