import streamlit as st
from datetime import date
from models import Cliente, Funcionario, Cargo, Profissao, Telefone, Endereco

st.title("👤 Sistema de Pessoas")

menu = st.sidebar.selectbox("Menu", [
    "Cadastrar Cliente",
    "Cadastrar Funcionário"
])

# Estado
if "pessoas" not in st.session_state:
    st.session_state.pessoas = []

# ---------------- CLIENTE ----------------
if menu == "Cadastrar Cliente":
    st.header("Cliente")

    nome = st.text_input("Nome")
    nasc = st.date_input("Data de nascimento")
    cod = st.number_input("Código", step=1)
    limite = st.number_input("Limite de crédito")

    profissao_nome = st.text_input("Profissão")

    if st.button("Salvar Cliente"):
        cliente = Cliente(nome, nasc, cod, limite)

        if profissao_nome:
            cliente.adicionar_profissao(Profissao(1, profissao_nome))

        cliente.adicionar_telefone(Telefone(83, 99999999))
        cliente.adicionar_endereco(Endereco("Rua A", "Centro", 10, "58000-000"))

        st.session_state.pessoas.append(cliente)
        st.success("Cliente cadastrado!")

# ---------------- FUNCIONARIO ----------------
elif menu == "Cadastrar Funcionário":
    st.header("Funcionário")

    nome = st.text_input("Nome")
    nasc = st.date_input("Nascimento")
    matricula = st.number_input("Matrícula", step=1)
    salario = st.number_input("Salário")

    cargo_nome = st.text_input("Cargo")

    if st.button("Salvar Funcionário"):
        cargo = Cargo(1, cargo_nome)
        func = Funcionario(nome, nasc, matricula, salario, date.today(), cargo)

        func.adicionar_telefone(Telefone(83, 88888888))
        func.adicionar_endereco(Endereco("Rua B", "Centro", 20, "58000-000"))

        st.session_state.pessoas.append(func)
        st.success("Funcionário cadastrado!")

# ---------------- LISTAGEM ----------------
st.header("📋 Pessoas")

for p in st.session_state.pessoas:
    st.write(f"{p.nome} - {p.calcular_idade()} anos")