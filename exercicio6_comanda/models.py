from datetime import datetime

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco


class ItemComanda:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = produto.preco

    def get_subtotal(self):
        return self.quantidade * self.preco_unitario


class Comanda:
    def __init__(self, numero):
        self.numero = numero
        self.abertura = datetime.now()
        self.status = "ABERTA"
        self.itens = []

    def adicionar_item(self, item: ItemComanda):
        if self.status == "PAGO":
            raise Exception("Comanda já fechada!")
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.get_subtotal() for item in self.itens)

    def fechar_conta(self, taxa=0):
        total = self.calcular_total()
        total_final = total + taxa

        # Simulação de atomicidade
        try:
            self.status = "PAGO"
            return total_final
        except:
            self.status = "ABERTA"
            raise Exception("Erro ao fechar comanda")