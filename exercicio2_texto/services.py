from models import TextoSaida

def gerar_html(texto_saida: TextoSaida, conteudo: str):
    css = texto_saida.obter_css()
    tipo = texto_saida.tipo.value

    if tipo == "label":
        return f'<div style="{css}">{conteudo}</div>'

    elif tipo == "input":
        return f'<input style="{css}" value="{conteudo}" />'

    elif tipo == "textarea":
        return f'<textarea style="{css}">{conteudo}</textarea>'