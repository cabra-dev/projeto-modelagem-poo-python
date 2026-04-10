from enums import CorEnum, TipoComponenteEnum

class TextoSaida:

    def __init__(self, tamanho_letra: int,
                 cor_fonte: CorEnum,
                 cor_fundo: CorEnum,
                 tipo: TipoComponenteEnum):

        self.tamanho_letra = tamanho_letra
        self.cor_fonte = cor_fonte
        self.cor_fundo = cor_fundo
        self.tipo = tipo

    def configurar(self, tamanho, cor_fonte, cor_fundo, tipo):
        self.tamanho_letra = tamanho
        self.cor_fonte = cor_fonte
        self.cor_fundo = cor_fundo
        self.tipo = tipo

    def obter_css(self):
        return f"""
        color: {self.cor_fonte.value};
        background-color: {self.cor_fundo.value};
        font-size: {self.tamanho_letra}px;
        padding: 10px;
        border-radius: 5px;
        """