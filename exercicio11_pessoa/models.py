from datetime import date

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero


class Endereco:
    def __init__(self, logradouro, bairro, numero, cep):
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.cep = cep


# ---------------- BASE ----------------
class Pessoa:
    def __init__(self, nome, data_nasc):
        self.nome = nome
        self.data_nasc = data_nasc
        self.telefones = []
        self.enderecos = []

    def calcular_idade(self):
        hoje = date.today()
        return hoje.year - self.data_nasc.year - (
            (hoje.month, hoje.day) < (self.data_nasc.month, self.data_nasc.day)
        )

    def adicionar_telefone(self, telefone):
        self.telefones.append(telefone)

    def adicionar_endereco(self, endereco):
        self.enderecos.append(endereco)


# ---------------- CLIENTE ----------------
class Profissao:
    def __init__(self, id_prof, nome):
        self.id_prof = id_prof
        self.nome = nome


class Cliente(Pessoa):
    def __init__(self, nome, data_nasc, cod_cli, limite_credito):
        super().__init__(nome, data_nasc)
        self.cod_cli = cod_cli
        self.limite_credito = limite_credito
        self.profissoes = []

    def adicionar_profissao(self, profissao):
        self.profissoes.append(profissao)


# ---------------- FUNCIONARIO ----------------
class Cargo:
    def __init__(self, id_cargo, nome):
        self.id_cargo = id_cargo
        self.nome = nome


class Funcionario(Pessoa):
    def __init__(self, nome, data_nasc, matricula, salario, data_admissao, cargo):
        super().__init__(nome, data_nasc)
        self.matricula = matricula
        self.salario = salario
        self.data_admissao = data_admissao
        self.cargo = cargo

    def reajustar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)

    def promover(self, novo_cargo):
        self.cargo = novo_cargo