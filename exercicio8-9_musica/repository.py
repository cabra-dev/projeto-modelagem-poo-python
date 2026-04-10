from database import get_connection

def inserir_cd(titulo, ano, coletanea, duplo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cd (titulo, ano, coletanea, duplo)
        VALUES (?, ?, ?, ?)
    """, (titulo, ano, coletanea, duplo))

    conn.commit()
    conn.close()


def inserir_musica(nome, duracao):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO musica (nome, duracao)
        VALUES (?, ?)
    """, (nome, duracao))

    conn.commit()
    conn.close()


def inserir_musico(nome):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO musico (nome) VALUES (?)", (nome,))

    conn.commit()
    conn.close()


def vincular_cd_musica(cd_id, musica_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cd_musica (cd_id, musica_id)
        VALUES (?, ?)
    """, (cd_id, musica_id))

    conn.commit()
    conn.close()


def vincular_musica_musico(musica_id, musico_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO musica_musico (musica_id, musico_id)
        VALUES (?, ?)
    """, (musica_id, musico_id))

    conn.commit()
    conn.close()


def buscar_cds_por_musico(nome):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT cd.titulo
    FROM cd
    JOIN cd_musica ON cd.id = cd_musica.cd_id
    JOIN musica ON musica.id = cd_musica.musica_id
    JOIN musica_musico ON musica.id = musica_musico.musica_id
    JOIN musico ON musico.id = musica_musico.musico_id
    WHERE musico.nome LIKE ?
    """, (f"%{nome}%",))

    return cursor.fetchall()