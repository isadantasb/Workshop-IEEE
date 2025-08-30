
# Workshop-IEEE

## Descrição
Projeto de desenvolvimento de backend em Python usando Flask e SQLite para um frontend já existente. O backend implementa funcionalidades CRUD (Create, Read, Update, Delete) para **Universidades**, **Cursos** e **Disciplinas**.

## Funcionalidades
- Cadastro, edição e exclusão de **Universidades**
- Cadastro, edição e exclusão de **Cursos** vinculados às universidades
- Cadastro, edição e exclusão de **Disciplinas** vinculadas aos cursos
- Integração com frontend já existente via API REST

## Tecnologias utilizadas
- Python 3  
- Flask  
- SQLite  
- Flask-CORS  
- HTML, CSS e JavaScript (no frontend recebido)

## Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Workshop-IEEE.git
cd Workshop-IEEE/backend
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```


Instale as dependências:

```bash
pip install Flask Flask-CORS
```

Crie o banco de dados:

```bash
python criar_banco.py
```

Rode a aplicação:

```bash
python app.py
```

Acesse a API pelo navegador ou pelo frontend em http://127.0.0.1:5000/api/...
