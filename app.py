from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from models import criar_tabela
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB = 'database.db'

criar_tabela(DB)

@app.route('/')
def home():
    return 'API de Gerenciamento de Alunos está no ar!'


@app.route('/cadastrar_aluno', methods=['POST'])
def cadastrar_aluno():
    data = request.json

    # Converte de 'YYYY-MM-DD' para 'DD/MM/YYYY'
    data_nascimento_iso = data['data_nascimento']
    try:
        data_nascimento_br = datetime.strptime(data_nascimento_iso, '%Y-%m-%d').strftime('%d/%m/%Y')
    except ValueError:
        return jsonify({'erro': 'Data inválida. Use o formato YYYY-MM-DD.'}), 400

    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("""
    INSERT INTO alunos (nome, email, data_nascimento, cpf)
    VALUES (?, ?, ?, ?)
""", (data['nome'], data['email'], data_nascimento_br, data['cpf']))
    con.commit()
    con.close()

    return jsonify({'mensagem': 'Aluno cadastrado com sucesso'}), 201

@app.route('/buscar_alunos', methods=['GET'])
def buscar_alunos():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos")
    alunos = cur.fetchall()
    con.close()
    return jsonify([
        {
            "id": a[0],
            "nome": a[1],
            "email": a[2],
            "data_nascimento": a[3],
            "cpf": a[4]
        } for a in alunos
    ])


@app.route('/buscar_aluno/<cpf>', methods=['GET'])
def buscar_aluno_por_cpf(cpf):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos WHERE cpf = ?", (cpf,))
    aluno = cur.fetchone()
    con.close()

    if aluno:
        return jsonify({
            "id": aluno[0],
            "nome": aluno[1],
            "email": aluno[2],
            "data_nascimento": aluno[3],
            "cpf": aluno[4]
        })

    return jsonify({"erro": "Aluno não encontrado"}), 404


@app.route('/deletar_aluno/<cpf>', methods=['DELETE'])
def deletar_aluno(cpf):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("DELETE FROM alunos WHERE cpf = ?", (cpf,))
    con.commit()
    con.close()
    return jsonify({"mensagem": "Aluno excluído com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
