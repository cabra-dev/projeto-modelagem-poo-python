from datetime import datetime, timedelta

class Remedio:
    def __init__(self, nome, principio_ativo, data_fabricacao, data_validade):
        self.nome = nome
        self.principio_ativo = principio_ativo
        self.data_fabricacao = data_fabricacao
        self.data_validade = data_validade


class Dose:
    def __init__(self, horario_previsto):
        self.horario_previsto = horario_previsto
        self.horario_tomado = None
        self.foi_tomado = False
        self.esta_atrasada = False

    def confirmar_ingestao(self, horario_real):
        self.horario_tomado = horario_real
        self.foi_tomado = True

        if horario_real > self.horario_previsto:
            self.esta_atrasada = True


class Prescricao:
    def __init__(self, paciente, remedio, data_inicio, dias, vezes_dia, dosagem):
        self.paciente = paciente
        self.remedio = remedio
        self.data_inicio = data_inicio
        self.dias = dias
        self.vezes_dia = vezes_dia
        self.dosagem = dosagem
        self.grade_horario = []

    def gerar_grade_inicial(self):
        intervalo = 24 // self.vezes_dia

        for dia in range(self.dias):
            for i in range(self.vezes_dia):
                horario = self.data_inicio + timedelta(days=dia, hours=i * intervalo)
                self.grade_horario.append(Dose(horario))

    def reorganizar_horarios(self, dose_atrasada):
        novo_inicio = dose_atrasada.horario_tomado
        intervalo = 24 // self.vezes_dia

        novas_doses = []

        for i in range(len(self.grade_horario)):
            horario = novo_inicio + timedelta(hours=i * intervalo)
            novas_doses.append(Dose(horario))

        self.grade_horario = novas_doses