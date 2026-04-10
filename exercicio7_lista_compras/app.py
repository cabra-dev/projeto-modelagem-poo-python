import streamlit as st
from models import ListaCompra, ItemCompra, Produto, UnidadeMedida
from services import resumo_lista

st.title("🛒 Lista de Compras")

# Estado
if "lista" not in st.session_state:
    st.session_state.lista = ListaCompra("2026-04")

lista = st.session_state.lista

# Cadastro
st.header("Adicionar Item")

nome = st.text_input("Produto")
qtd_prev = st.number_input("Qtd Prevista", 0.0)
preco = st.number_input("Preço Estimado", 0.0)

if st.button("Adicionar"):
    produto = Produto(nome)
    unidade = UnidadeMedida("UN", "Unidade")

    item = ItemCompra(produto, unidade, qtd_prev, preco)
    lista.adicionar_item(item)

    st.success("Item adicionado!")

# Atualizar compra real
st.header("Atualizar Compra Real")

for i, item in enumerate(lista.itens):
    st.subheader(item.produto.nome)

    item.qtd_efetiva = st.number_input(
        f"Qtd Real {i}", value=item.qtd_efetiva, key=f"qtd{i}"
    )

    novo_preco = st.number_input(
        f"Preço Real {i}", value=item.preco_real, key=f"preco{i}"
    )

    if st.button(f"Atualizar {i}"):
        item.atualizar_preco(novo_preco)
        st.success("Atualizado!")

# Relatório
st.header("📊 Resumo")

st.write(f"Total Previsto: R$ {lista.get_total_previsto():.2f}")
st.write(f"Total Real: R$ {lista.get_total_real():.2f}")
st.write(f"Diferença: R$ {lista.get_diferenca_orcamento():.2f}")

# Clonar lista
if st.button("Clonar Lista"):
    nova = lista.clonar()
    st.session_state.lista = nova
    st.success("Lista clonada!")