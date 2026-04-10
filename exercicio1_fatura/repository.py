from database import get_connection

def inserir_leitura(data, numero, kwh):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leitura (data_leitura, numero_leitura, kwh_gasto)
        VALUES (?, ?, ?)
    """, (data, numero, kwh))

    conn.commit()
    conn.close()


def listar_leituras():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leitura ORDER BY data_leitura")
    dados = cursor.fetchall()

    conn.close()
    return dados


def inserir_fatura(data_emissao, data_vencimento, valor, leitura_i, leitura_f):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO fatura 
        (data_emissao, data_vencimento, valor_total, leitura_inicial_id, leitura_final_id, status_pagamento)
        VALUES (?, ?, ?, ?, ?, 'PENDENTE')
    """, (data_emissao, data_vencimento, valor, leitura_i, leitura_f))

    conn.commit()
    conn.close()


def registrar_pagamento(data_pagamento, valor, fatura_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pagamento (data_pagamento, valor_pago, fatura_id)
        VALUES (?, ?, ?)
    """, (data_pagamento, valor, fatura_id))

    cursor.execute("""
        UPDATE fatura SET status_pagamento = 'PAGO'
        WHERE id = ?
    """, (fatura_id,))

    conn.commit()
    conn.close()