import streamlit as st
from enums import CorEnum, TipoComponenteEnum
from models import TextoSaida
from services import gerar_html

st.title("🎨 Configurador de Texto")

# Inputs
tamanho = st.slider("Tamanho da fonte", 10, 50, 16)

cor_fonte = st.selectbox("Cor da fonte", list(CorEnum))
cor_fundo = st.selectbox("Cor de fundo", list(CorEnum))
tipo = st.selectbox("Tipo de componente", list(TipoComponenteEnum))

conteudo = st.text_input("Texto", "Exemplo de texto")

# Criar objeto
texto = TextoSaida(tamanho, cor_fonte, cor_fundo, tipo)

# Gerar HTML
html = gerar_html(texto, conteudo)

st.markdown("### Resultado:")
st.markdown(html, unsafe_allow_html=True)