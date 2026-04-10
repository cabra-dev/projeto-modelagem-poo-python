from enums import CategoriaGasto, FormaPagamento
from datetime import date

class Gasto:
    def __init__(self, data, valor, categoria, pagamento):
        self.data = data
        self.valor = valor
        self.categoria = categoria
        self.pagamento = pagamento


class ControleMensal:
    def __init__(self, mes, ano):
        self.mes = mes
        self.ano = ano
        self.gastos = []

    def registrar_gasto(self, gasto: Gasto):
        self.gastos.append(gasto)

    def calcular_total_mes(self):
        return sum(g.valor for g in self.gastos)

    def calcular_total_por_categoria(self, categoria):
        return sum(g.valor for g in self.gastos if g.categoria == categoria)

    def calcular_total_por_pagamento(self, pagamento):
        return sum(g.valor for g in self.gastos if g.pagamento == pagamento)