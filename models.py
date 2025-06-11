import sqlite3

def criar_tabela(db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        data_nascimento TEXT,
        cpf TEXT UNIQUE NOT NULL
    )
""")
    con.commit()
    con.close()
