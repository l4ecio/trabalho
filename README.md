#  Projeto: API Simples de Usuários com FastAPI

Este é um projeto simples feito com **FastAPI** para simular o cadastro e listagem de usuários.

##  Tecnologias Utilizadas
- Python 3.10+
- FastAPI
- Uvicorn
- Pytest

##  Instalação

1. Clone o repositório ou baixe os arquivos:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶ Como Rodar a API

```bash
uvicorn main:app --reload
```

Abra no navegador: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

##  Como Rodar os Testes

```bash
pytest -v
```

##  Funcionalidades
- `POST /users`: Cadastra usuário
- `GET /users`: Lista usuários
- `GET /users/{id}`: Busca por ID

##  Observações
- Dados em memória
- Testes com fixtures, parametrize e skip
