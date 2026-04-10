import streamlit as st
from models import Boneco
from enums import Direcao

st.title("🎮 Controle do Boneco (WASD)")

# Estado persistente
if "boneco" not in st.session_state:
    st.session_state.boneco = Boneco("Player", 50, 50)

boneco = st.session_state.boneco

# Controles estilo teclado
col1, col2, col3 = st.columns(3)

with col2:
    if st.button("⬆️ (W)"):
        boneco.mover(Direcao.CIMA, 5)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ (A)"):
        boneco.mover(Direcao.ESQUERDA, 5)

with col2:
    if st.button("⬇️ (S)"):
        boneco.mover(Direcao.BAIXO, 5)

with col3:
    if st.button("➡️ (D)"):
        boneco.mover(Direcao.DIREITA, 5)

# Mostrar posição
x, y, direcao = boneco.obter_posicao_atual()

st.write(f"📍 X: {x} | Y: {y} | Direção: {direcao}")

# Mapa visual
st.markdown("### 🗺️ Mapa")

grid_size = 10
mapa = [["⬜" for _ in range(grid_size)] for _ in range(grid_size)]

pos_x = min(x // 10, grid_size - 1)
pos_y = min(y // 10, grid_size - 1)

mapa[grid_size - 1 - pos_y][pos_x] = "🟥"

for linha in mapa:
    st.write(" ".join(linha))