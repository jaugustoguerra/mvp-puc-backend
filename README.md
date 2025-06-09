# 🎓 Back-end - API Gerenciador de Alunos

Este projeto é a API do sistema de gerenciamento de alunos, desenvolvida com Python, Flask e SQLite. Ela permite cadastrar, listar, buscar por ID e deletar alunos, além de estar documentada com Swagger (OpenAPI).

## 🚀 Funcionalidades

- ✅ Cadastrar aluno
- 🔍 Listar todos os alunos
- 🔎 Buscar aluno por ID
- ❌ Deletar aluno
- 📑 Documentação Swagger

## 🛠️ Tecnologias

- Python 3
- Flask
- Flask-CORS
- SQLite
- Swagger (OpenAPI)

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/jaugustoguerra/mvp-puc-backend
cd mvp-puc-backend

# Crie e ative o ambiente virtual (opcional)
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor Flask
python app.py
```

A API estará disponível em: `http://localhost:5000`

## 📚 Como usar o Swagger

1. Acesse: [https://editor.swagger.io](https://editor.swagger.io)
2. Cole o conteúdo do arquivo `swagger.yaml`
3. Verifique que o campo `servers` está definido como:
```yaml
servers:
  - url: http://localhost:5000
```
4. Clique em “Try it out” nas rotas e execute!

## 📂 Estrutura

```
/back-end
├── app.py
├── models.py
├── database.db
├── requirements.txt
└── swagger.yaml
```

## 👨‍💻 Autor

Desenvolvido por José Augusto Guerra da Silva.
