import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Universidades(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               sigla TEXT NOT NULL,
               data_criacao DATE NOT NULL,
               publica INTEGER NOT NULL)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Cursos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               nivel TEXT NOT NULL,
               duracao INTEGER NOT NULL,
               universidade_id INTEGER NOT NULL,
               FOREIGN KEY(universidade_id) REFERENCES Universidades(id)
               )''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Disciplinas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               carga_horaria INTEGER NOT NULL, 
               curso_id INTEGER NOT NULL,
               semestre TEXT CHECK(semestre IN ('1','2','')) DEFAULT '',
               FOREIGN KEY(curso_id) REFERENCES Cursos(id)
               )''') 


print('Banco criado')

conexao.commit()
conexao.close()