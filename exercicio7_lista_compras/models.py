class UnidadeMedida:
    def __init__(self, sigla, descricao):
        self.sigla = sigla
        self.descricao = descricao


class Produto:
    def __init__(self, nome):
        self.nome = nome


class ItemCompra:
    def __init__(self, produto, unidade, qtd_prevista, preco_estimado):
        self.produto = produto
        self.unidade = unidade
        self.qtd_prevista = qtd_prevista
        self.qtd_efetiva = 0
        self.preco_estimado = preco_estimado
        self.preco_real = preco_estimado

    def atualizar_preco(self, novo_preco):
        self.preco_real = novo_preco

    def total_previsto(self):
        return self.qtd_prevista * self.preco_estimado

    def total_real(self):
        return self.qtd_efetiva * self.preco_real


class ListaCompra:
    def __init__(self, identificador_mes):
        self.identificador_mes = identificador_mes
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def get_total_previsto(self):
        return sum(i.total_previsto() for i in self.itens)

    def get_total_real(self):
        return sum(i.total_real() for i in self.itens)

    def get_diferenca_orcamento(self):
        return self.get_total_real() - self.get_total_previsto()

    def clonar(self):
        nova_lista = ListaCompra(self.identificador_mes + "_copia")
        for item in self.itens:
            novo_item = ItemCompra(
                item.produto,
                item.unidade,
                item.qtd_prevista,
                item.preco_estimado
            )
            nova_lista.adicionar_item(novo_item)
        return nova_lista