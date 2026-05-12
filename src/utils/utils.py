from deep_translator import GoogleTranslator

def traduzir(texto: str, origem: str, destino: str) -> str:
    return GoogleTranslator(source=origem, target=destino).translate(texto)