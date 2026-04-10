import streamlit as st
from datetime import date
from models import ControleMensal, Gasto
from enums import CategoriaGasto, FormaPagamento
from services import agrupar_por_categoria, agrupar_por_pagamento

st.title("💰 Controle de Gastos")

# Estado
if "controle" not in st.session_state:
    hoje = date.today()
    st.session_state.controle = ControleMensal(hoje.month, hoje.year)

controle = st.session_state.controle

# Cadastro
st.header("Registrar Gasto")

data = st.date_input("Data", date.today())
valor = st.number_input("Valor", min_value=0.0, step=0.01)

categoria = st.selectbox("Categoria", list(CategoriaGasto))
pagamento = st.selectbox("Forma de pagamento", list(FormaPagamento))

if st.button("Adicionar"):
    gasto = Gasto(data, valor, categoria, pagamento)
    controle.registrar_gasto(gasto)
    st.success("Gasto registrado!")

# Relatórios
st.header("📊 Relatórios")

st.subheader("Total do mês")
st.write(f"R$ {controle.calcular_total_mes():.2f}")

st.subheader("Por Categoria")
cat_data = agrupar_por_categoria(controle)
st.write(cat_data)

st.subheader("Por Forma de Pagamento")
pag_data = agrupar_por_pagamento(controle)
st.write(pag_data)