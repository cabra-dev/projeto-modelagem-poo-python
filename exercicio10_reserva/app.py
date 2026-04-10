import streamlit as st
from datetime import date, time
from models import Sala, Funcionario, Reserva
from services import verificar_conflito, salas_disponiveis

st.title("🏢 Sistema de Reservas")

# Mock
salas = [Sala("101"), Sala("102"), Sala("103")]
funcionario = Funcionario("Eduardo", "Dev", 1)

# Estado
if "reservas" not in st.session_state:
    st.session_state.reservas = []

reservas = st.session_state.reservas

menu = st.sidebar.selectbox("Menu", [
    "Nova Reserva",
    "Consultar Salas Livres",
    "Ver Reservas"
])

# -------------------
if menu == "Nova Reserva":
    st.header("Agendar Reunião")

    data = st.date_input("Data", date.today())
    inicio = st.time_input("Início")
    fim = st.time_input("Fim")
    assunto = st.text_input("Assunto")

    sala = st.selectbox("Sala", salas, format_func=lambda x: x.numero)

    if st.button("Agendar"):
        nova = Reserva(data, inicio, fim, assunto, sala, funcionario)

        if verificar_conflito(reservas, nova):
            st.error("❌ Sala já ocupada nesse horário!")
        else:
            reservas.append(nova)
            st.success("Reserva criada!")

# -------------------
elif menu == "Consultar Salas Livres":
    st.header("Salas Disponíveis")

    data = st.date_input("Data")
    inicio = st.time_input("Início")
    fim = st.time_input("Fim")

    if st.button("Buscar"):
        livres = salas_disponiveis(reservas, salas, data, inicio, fim)

        for sala in livres:
            st.write(f"Sala {sala.numero}")

# -------------------
elif menu == "Ver Reservas":
    st.header("📅 Reservas")

    for r in reservas:
        st.write(
            f"Sala {r.sala.numero} | {r.data} {r.inicio}-{r.fim} | {r.assunto}"
        )