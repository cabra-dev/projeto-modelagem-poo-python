import streamlit as st
from datetime import datetime
from models import Prescricao, Remedio

st.title("💊 Controle de Remédios")

# Estado
if "prescricao" not in st.session_state:
    st.session_state.prescricao = None

# Cadastro
st.header("Cadastrar Prescrição")

paciente = st.text_input("Paciente")
nome_remedio = st.text_input("Remédio")
principio = st.text_input("Princípio ativo")

dias = st.number_input("Dias de tratamento", 1, 30, 5)
vezes = st.number_input("Vezes ao dia", 1, 6, 3)
dosagem = st.text_input("Dosagem", "500mg")

if st.button("Criar Prescrição"):
    remedio = Remedio(nome_remedio, principio, datetime.now(), datetime.now())
    prescricao = Prescricao(paciente, remedio, datetime.now(), dias, vezes, dosagem)
    prescricao.gerar_grade_inicial()

    st.session_state.prescricao = prescricao
    st.success("Prescrição criada!")

# Mostrar doses
if st.session_state.prescricao:
    prescricao = st.session_state.prescricao

    st.header("📅 Grade de Doses")

    for i, dose in enumerate(prescricao.grade_horario):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(dose.horario_previsto.strftime("%d/%m %H:%M"))

        with col2:
            if dose.foi_tomado:
                st.success("Tomado")
            elif dose.esta_atrasada:
                st.error("Atrasado")
            else:
                st.warning("Pendente")

        with col3:
            if not dose.foi_tomado:
                if st.button(f"Tomar {i}"):
                    agora = datetime.now()
                    dose.confirmar_ingestao(agora)

                    if dose.esta_atrasada:
                        prescricao.reorganizar_horarios(dose)

                    st.rerun()