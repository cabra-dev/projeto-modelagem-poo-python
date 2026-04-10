import streamlit as st
from database import create_tables
import repository as repo

create_tables()

st.title("🎵 Sistema de CDs")

menu = st.sidebar.selectbox("Menu", [
    "Cadastrar CD",
    "Cadastrar Música",
    "Cadastrar Músico",
    "Buscar CDs por Músico"
])

# -------------------
if menu == "Cadastrar CD":
    titulo = st.text_input("Título")
    ano = st.number_input("Ano", 1900, 2100)
    coletanea = st.checkbox("Coletânea")
    duplo = st.checkbox("Duplo")

    if st.button("Salvar CD"):
        repo.inserir_cd(titulo, ano, coletanea, duplo)
        st.success("CD cadastrado!")

# -------------------
elif menu == "Cadastrar Música":
    nome = st.text_input("Nome")
    duracao = st.text_input("Duração (ex: 3:45)")

    if st.button("Salvar Música"):
        repo.inserir_musica(nome, duracao)
        st.success("Música cadastrada!")

# -------------------
elif menu == "Cadastrar Músico":
    nome = st.text_input("Nome do músico")

    if st.button("Salvar"):
        repo.inserir_musico(nome)
        st.success("Músico cadastrado!")

# -------------------
elif menu == "Buscar CDs por Músico":
    nome = st.text_input("Nome do músico")

    if st.button("Buscar"):
        resultados = repo.buscar_cds_por_musico(nome)

        for r in resultados:
            st.write(r[0])