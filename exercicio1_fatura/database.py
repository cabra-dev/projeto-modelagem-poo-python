import sqlite3

def get_connection():
    conn = sqlite3.connect("energia.db", check_same_thread=False)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leitura (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_leitura TEXT,
        numero_leitura INTEGER,
        kwh_gasto REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fatura (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_emissao TEXT,
        data_vencimento TEXT,
        valor_total REAL,
        leitura_inicial_id INTEGER,
        leitura_final_id INTEGER,
        status_pagamento TEXT,
        FOREIGN KEY(leitura_inicial_id) REFERENCES leitura(id),
        FOREIGN KEY(leitura_final_id) REFERENCES leitura(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_pagamento TEXT,
        valor_pago REAL,
        fatura_id INTEGER UNIQUE,
        FOREIGN KEY(fatura_id) REFERENCES fatura(id)
    )
    """)

    conn.commit()
    conn.close()