from enum import Enum

class CategoriaGasto(Enum):
    REMEDIO = "Remédio"
    ROUPA = "Roupa"
    REFEICAO = "Refeição"
    OUTROS = "Outros"


class FormaPagamento(Enum):
    DINHEIRO = "Dinheiro"
    CARTAO_CREDITO = "Cartão de Crédito"
    CARTAO_DEBITO = "Cartão de Débito"
    PIX = "Pix"