import streamlit as st
from datetime import date
from database import create_tables
import repository as repo
from decimal import Decimal

create_tables()

st.title("⚡ Sistema de Energia")

menu = st.sidebar.selectbox("Menu", [
    "Registrar Leitura",
    "Gerar Fatura",
    "Registrar Pagamento",
    "Relatórios"
])

# ---------------------------
if menu == "Registrar Leitura":
    st.header("Nova Leitura")

    data = st.date_input("Data", date.today())
    numero = st.number_input("Número da leitura", step=1)
    kwh = st.number_input("Consumo (kWh)", step=1.0)

    if st.button("Salvar"):
        repo.inserir_leitura(str(data), numero, kwh)
        st.success("Leitura registrada!")

# ---------------------------
elif menu == "Gerar Fatura":
    st.header("Gerar Fatura")

    leituras = repo.listar_leituras()

    if len(leituras) < 2:
        st.warning("Precisa de pelo menos 2 leituras.")
    else:
        l1 = st.selectbox("Leitura Inicial", leituras)
        l2 = st.selectbox("Leitura Final", leituras)

        if st.button("Gerar"):
            consumo = l2[3] - l1[3]
            valor = Decimal(consumo) * Decimal("0.80")

            repo.inserir_fatura(
                str(date.today()),
                str(date.today()),
                float(valor),
                l1[0],
                l2[0]
            )

            st.success(f"Fatura gerada: R$ {valor}")

# ---------------------------
elif menu == "Registrar Pagamento":
    st.header("Pagamento")

    fatura_id = st.number_input("ID da Fatura", step=1)
    valor = st.number_input("Valor pago", step=0.01)

    if st.button("Pagar"):
        repo.registrar_pagamento(str(date.today()), valor, fatura_id)
        st.success("Pagamento registrado!")

# ---------------------------
elif menu == "Relatórios":
    st.header("Relatórios")

    leituras = repo.listar_leituras()
    consumos = [l[3] for l in leituras]

    if consumos:
        st.write("📊 Média:", sum(consumos)/len(consumos))
        st.write("📈 Maior:", max(consumos))
        st.write("📉 Menor:", min(consumos))
    else:
        st.warning("Sem dados.")