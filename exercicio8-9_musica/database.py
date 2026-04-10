import sqlite3

def get_connection():
    conn = sqlite3.connect("musica.db", check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cd (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        ano INTEGER,
        coletanea BOOLEAN,
        duplo BOOLEAN
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS musica (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        duracao TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS musico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
    """)

    # Relacionamentos N:N
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cd_musica (
        cd_id INTEGER,
        musica_id INTEGER,
        FOREIGN KEY(cd_id) REFERENCES cd(id) ON DELETE CASCADE,
        FOREIGN KEY(musica_id) REFERENCES musica(id) ON DELETE CASCADE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS musica_musico (
        musica_id INTEGER,
        musico_id INTEGER,
        FOREIGN KEY(musica_id) REFERENCES musica(id) ON DELETE CASCADE,
        FOREIGN KEY(musico_id) REFERENCES musico(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()