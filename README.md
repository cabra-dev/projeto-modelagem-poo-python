# 📚 Projeto: Exercícios de Modelagem e Desenvolvimento com Python + Streamlit

## 📌 Sobre o Projeto

Este repositório reúne uma coleção de **sistemas desenvolvidos a partir de diagramas UML e requisitos funcionais e não funcionais**, com o objetivo de aplicar conceitos de:

* Programação Orientada a Objetos (POO)
* Modelagem de Sistemas
* Regras de Negócio
* Estruturação de Projetos
* Desenvolvimento de Interfaces com Streamlit

Cada exercício representa um **mini sistema independente**, simulando cenários reais de mercado.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **Streamlit**
* **SQLite (em alguns exercícios)**
* **Programação Orientada a Objetos (POO)**
* **Enums, Herança, Composição**
* **Boas práticas de organização de código**

---

## 📂 Estrutura do Repositório

```
📦 projeto
 ┣ 📂 exercicio1_fatura
 ┣ 📂 exercicio2_texto
 ┣ 📂 exercicio3_boneco
 ┣ 📂 exercicio4_remedios
 ┣ 📂 exercicio5_gastos
 ┣ 📂 exercicio6_comanda
 ┣ 📂 exercicio7_lista_compra
 ┣ 📂 exercicio8-9_musica
 ┣ 📂 exercicio10_reserva
 ┣ 📂 exercicio11_pessoa
 ┗ 📄 README.md
```

Cada pasta contém:

* `app.py` → Interface (Streamlit)
* `models.py` → Entidades do sistema
* `services.py` → Regras de negócio
* `enums.py` → (quando aplicável)
* `database.py / repository.py` → (quando necessário)

---

## 🧩 Exercícios Desenvolvidos

### 1️⃣ Sistema de Faturas

* Registro de leituras
* Geração de faturas
* Controle de pagamentos
* Relatórios de consumo

---

### 2️⃣ Componente de Texto Dinâmico

* Configuração de estilo (cor, tamanho, tipo)
* Uso de Enums
* Geração de CSS dinâmico

---

### 3️⃣ Controle de Movimento (Boneco)

* Movimentação em plano cartesiano
* Controle por direção
* Limites de tela

---

### 4️⃣ Controle de Medicamentos

* Geração automática de horários
* Controle de doses
* Reorganização em caso de atraso

---

### 5️⃣ Controle de Gastos Mensais

* Registro de despesas
* Relatórios por categoria e pagamento
* Total mensal

---

### 6️⃣ Sistema de Comandas

* Registro de pedidos
* Cálculo de total
* Fechamento de conta

---

### 7️⃣ Lista de Compras Inteligente

* Planejamento vs execução
* Controle de preços
* Clonagem de listas

---

### 8️⃣ Sistema de CDs e Músicas

* Relacionamento N:N
* Cadastro de artistas e músicas
* Consultas cruzadas

---

### 9️⃣ Sistema de Reserva de Salas

* Agendamento de reuniões
* Verificação de conflitos
* Consulta de disponibilidade

---

### 🔟 Sistema de Pessoas (Cliente/Funcionário)

* Herança (Pessoa base)
* Cadastro unificado
* Cálculo de idade
* Regras específicas por tipo

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
```

2. Acesse a pasta de um exercício:

```bash
cd exercicioX_nome
```

3. Instale as dependências:

```bash
pip install streamlit
```

4. Execute o projeto:

```bash
python -m streamlit run app.py
```

---

## 📊 Conceitos Aplicados

* ✔ Programação Orientada a Objetos (POO)
* ✔ Herança e Polimorfismo
* ✔ Encapsulamento
* ✔ Separação de responsabilidades (MVC-like)
* ✔ Uso de Enums para segurança de dados
* ✔ Validações de regras de negócio
* ✔ Modelagem baseada em UML

---

## ⚠️ Melhorias Futuras

* Implementação de autenticação de usuários
* Persistência completa em banco de dados
* Dashboards com gráficos
* Deploy em ambiente cloud
* Testes automatizados

---

## 👨‍💻 Autor

Projeto desenvolvido por **Eduardo**
📍 João Pessoa - PB

---

## 📌 Observação

Este projeto foi desenvolvido com fins acadêmicos e demonstra a aplicação prática de conceitos fundamentais de engenharia de software.

---

⭐ Se este projeto te ajudou ou te inspirou, deixe uma estrela!
