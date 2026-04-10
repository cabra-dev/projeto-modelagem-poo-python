from enums import Direcao

class Boneco:

    def __init__(self, nome: str, x: int, y: int):
        self.nome = nome
        self.x = x
        self.y = y
        self.direcao_atual = Direcao.CIMA

    def mover(self, direcao: Direcao, passos: int, limite_x=100, limite_y=100):
        self.direcao_atual = direcao

        if direcao == Direcao.CIMA:
            self.y = min(self.y + passos, limite_y)

        elif direcao == Direcao.BAIXO:
            self.y = max(self.y - passos, 0)

        elif direcao == Direcao.DIREITA:
            self.x = min(self.x + passos, limite_x)

        elif direcao == Direcao.ESQUERDA:
            self.x = max(self.x - passos, 0)

    def obter_posicao_atual(self):
        return (self.x, self.y, self.direcao_atual.value)