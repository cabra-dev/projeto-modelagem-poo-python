import streamlit as st
from models import Produto, ItemComanda, Comanda
from services import resumo_comanda

st.title("🍞 Sistema de Comanda")

# Produtos mockados
produtos = [
    Produto(1, "Pão", 1.50),
    Produto(2, "Café", 3.00),
    Produto(3, "Bolo", 5.00)
]

# Estado
if "comanda" not in st.session_state:
    st.session_state.comanda = Comanda(1)

comanda = st.session_state.comanda

# Adicionar item
st.header("Adicionar Item")

produto = st.selectbox("Produto", produtos, format_func=lambda x: x.nome)
qtd = st.number_input("Quantidade", 1, 10, 1)

if st.button("Adicionar"):
    item = ItemComanda(produto, qtd)
    comanda.adicionar_item(item)
    st.success("Item adicionado!")

# Mostrar itens
st.header("🧾 Itens da Comanda")

dados = resumo_comanda(comanda)

for d in dados:
    st.write(f"{d['produto']} - {d['qtd']}x = R$ {d['subtotal']:.2f}")

# Total
total = comanda.calcular_total()
st.write(f"### 💰 Total: R$ {total:.2f}")

# Fechar conta
taxa = st.number_input("Taxa adicional", 0.0, step=0.5)

if st.button("Fechar Conta"):
    total_final = comanda.fechar_conta(taxa)
    st.success(f"Conta fechada! Total final: R$ {total_final:.2f}")