import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_conexaodb():
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route('/api/universidades', methods = ['GET'])
def get_universidades():
    conexao = get_conexaodb()
    universidades_cursor = conexao.execute('SELECT * FROM Universidades').fetchall()
    universidades = [dict(row) for row in universidades_cursor]
    conexao.close()

    return jsonify(universidades)

@app.route('/api/universidades', methods = ['POST'])
def add_universidade():
    nova_uni = request.get_json()
    nome = nova_uni['nome']
    sigla = nova_uni['sigla']
    data_criacao = nova_uni['data_criacao']
    publica = nova_uni['publica']
    conexao = get_conexaodb()
    conexao.execute('INSERT INTO Universidades(nome, sigla, data_criacao, publica) VALUES (?, ?, ?, ?)',
                    (nome,sigla, data_criacao, publica))
    conexao.commit()
    conexao.close()
    return jsonify({'message': 'Universidade adicionada!'}), 201

@app.route('/api/universidades/<int:id>', methods = ['PUT'])
def update_universidade(id):
    uni_atualizada = request.get_json()
    nome = uni_atualizada['nome']
    sigla = uni_atualizada['sigla']
    data_criacao = uni_atualizada['data_criacao']
    publica = uni_atualizada['publica']
    conexao = get_conexaodb()
    conexao.execute('UPDATE Universidades SET nome = ?, sigla = ?, data_criacao = ?, publica = ? WHERE id = ?',
                    (nome, sigla, data_criacao, publica, id))
    conexao.commit()
    conexao.close()
    return jsonify({'message':'Universidade atualizada!'})

@app.route('/api/universidades/<int:id>', methods = ['DELETE'])
def delete_universidade(id):
    conexao = get_conexaodb()
    conexao.execute('DELETE FROM Universidades WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    return jsonify({'message': 'Universidade deletada'})

@app.route('/api/cursos', methods=['GET'])
def get_cursos():
    conexao = get_conexaodb()
    cursos_cursor = conexao.execute('''
        SELECT Cursos.id, Cursos.nome, Cursos.nivel, Cursos.duracao,
               Universidades.nome AS universidade_nome
        FROM Cursos
        JOIN Universidades ON Cursos.universidade_id = Universidades.id
    ''')
    cursos = [dict(row) for row in cursos_cursor]
    conexao.close()
    return jsonify(cursos)


@app.route('/api/cursos', methods = ['POST'])
def add_curso():
    novo_curso = request.get_json()
    nome = novo_curso['nome']
    nivel = novo_curso['nivel']
    duracao = novo_curso['duracao']
    universidade_id = novo_curso['universidade_id']
    print(novo_curso)
    conexao = get_conexaodb()    
    conexao.execute('INSERT INTO Cursos(nome, nivel, duracao, universidade_id) VALUES (?, ?, ?, ?)',
                    (nome, nivel, duracao, universidade_id))
    conexao.commit()
    conexao.close()
    return jsonify({'message': 'Curso adicionado!'}), 201

@app.route('/api/cursos/<int:id>', methods = ['PUT'])
def update_cursos(id):
    print('fala galera')
    curso_att = request.get_json()
    nome = curso_att['nome']
    nivel = curso_att['nivel']
    duracao = curso_att['duracao']
    universidade_id = curso_att['universidade_id']
    print(curso_att)
    conexao = get_conexaodb()
    conexao.execute('UPDATE Cursos SET nome = ?, nivel = ?, duracao = ?, universidade_id = ? WHERE id = ?',
                    (nome,nivel,duracao,universidade_id, id))
    conexao.commit()
    conexao.close()
    return jsonify({'message': 'Curso atualizado!'})

@app.route('/api/cursos/<int:id>', methods = ['DELETE'])
def delete_curso(id):
    conexao = get_conexaodb()
    conexao.execute('DELETE FROM Cursos WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    return jsonify({'message': 'Curso deletado!'})

@app.route('/api/disciplinas', methods=['GET'])
def get_disciplinas():
    conexao = get_conexaodb()
    disciplinas_cursor = conexao.execute('SELECT * FROM Disciplinas')
    disciplinas = [dict(row) for row in disciplinas_cursor]
    conexao.close()
    return jsonify(disciplinas)

@app.route('/api/disciplinas', methods=['POST'])
def add_disciplina():
    nova_disciplina = request.get_json()
    nome = nova_disciplina['nome']
    carga_horaria = nova_disciplina['carga_horaria']
    curso_id = nova_disciplina['curso_id']
    semestre = nova_disciplina['semestre']
    conexao = get_conexaodb()
    conexao.execute(
        'INSERT INTO Disciplinas (nome, carga_horaria, curso_id, semestre) VALUES (?, ?, ?, ?)',
        (nome, carga_horaria, curso_id, semestre)
    )
    conexao.commit()
    conexao.close()
    return jsonify({'message': 'Disciplina adicionada!'}), 201

@app.route('/api/disciplinas/<int:id>', methods=['PUT'])
def update_disciplina(id):
    disciplina_att = request.get_json()
    nome = disciplina_att['nome']
    carga_horaria = disciplina_att['carga_horaria']
    curso_id = disciplina_att['curso_id']
    semestre = disciplina_att['semestre']
    conexao = get_conexaodb()
    conexao.execute(
        'UPDATE Disciplinas SET nome = ?, carga_horaria = ?, curso_id = ?, semestre = ? WHERE id = ?',
        (nome, carga_horaria, curso_id, semestre, id)
    )
    conexao.commit()
    conexao.close()
    return jsonify({'message': 'Disciplina atualizada!'})

@app.route('/api/disciplinas/<int:id>', methods=['DELETE'])
def delete_disciplina(id):
    conexao = get_conexaodb()
    conexao.execute('DELETE FROM Disciplinas WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    return jsonify({'message': 'Disciplina deletada!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)