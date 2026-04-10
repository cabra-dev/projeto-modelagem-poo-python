from datetime import datetime

class Sala:
    def __init__(self, numero):
        self.numero = numero


class Funcionario:
    def __init__(self, nome, cargo, matricula):
        self.nome = nome
        self.cargo = cargo
        self.matricula = matricula


class Reserva:
    def __init__(self, data, inicio, fim, assunto, sala, funcionario):
        self.data = data
        self.inicio = inicio
        self.fim = fim
        self.assunto = assunto
        self.sala = sala
        self.funcionario = funcionario

    def remanejar(self, nova_data, novo_inicio, novo_fim, nova_sala):
        self.data = nova_data
        self.inicio = novo_inicio
        self.fim = novo_fim
        self.sala = nova_sala