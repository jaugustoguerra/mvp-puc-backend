from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from models import criar_tabela

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
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("INSERT INTO alunos (nome, email, data_nascimento) VALUES (?, ?, ?)",
                (data['nome'], data['email'], data['data_nascimento']))
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
    return jsonify([{"id": a[0], "nome": a[1], "email": a[2], "data_nascimento": a[3]} for a in alunos])

@app.route('/buscar_aluno/<int:id>', methods=['GET'])
def buscar_aluno(id):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos WHERE id = ?", (id,))
    aluno = cur.fetchone()
    con.close()
    if aluno:
        return jsonify({"id": aluno[0], "nome": aluno[1], "email": aluno[2], "data_nascimento": aluno[3]})
    return jsonify({"erro": "Aluno não encontrado"}), 404

@app.route('/deletar_aluno/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("DELETE FROM alunos WHERE id = ?", (id,))
    con.commit()
    con.close()
    return jsonify({"mensagem": "Aluno excluído com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
