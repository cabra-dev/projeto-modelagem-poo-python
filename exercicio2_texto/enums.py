from enum import Enum

class CorEnum(Enum):
    PRETO = "black"
    BRANCO = "white"
    AZUL = "blue"
    AMARELO = "yellow"
    CINZA = "gray"


class TipoComponenteEnum(Enum):
    LABEL = "label"
    EDIT = "input"
    MEMO = "textarea"