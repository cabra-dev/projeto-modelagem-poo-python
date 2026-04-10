from decimal import Decimal

class Leitura:
    def __init__(self, data, numero, kwh):
        self.data = data
        self.numero = numero
        self.kwh = kwh


class Fatura:
    def __init__(self, data_emissao, data_vencimento, leitura_inicial, leitura_final):
        self.data_emissao = data_emissao
        self.data_vencimento = data_vencimento
        self.leitura_inicial = leitura_inicial
        self.leitura_final = leitura_final
        self.valor_total = Decimal(0)
        self.status = "PENDENTE"

    def calcular_valor(self, tarifa=Decimal("0.80")):
        consumo = Decimal(self.leitura_final.kwh - self.leitura_inicial.kwh)
        self.valor_total = consumo * tarifa
        return self.valor_total

    def marcar_como_paga(self):
        self.status = "PAGO"