import sqlite3 as sq
import os
import sys
from pathlib import Path

# Adicionar o diretório principal ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from funcoes import func_global as fg

#Obtem o caminho do diretorio atual
diretorio_actual = os.path.dirname(__file__)
#Obtem o caminho do diretorio que contem o arquivo 
caminho_arquivo = os.path.join(diretorio_actual, '../banco_dados', 'curso.db')

fg.acessar_banco(caminho_arquivo)
#Função para criar tabela dos cursos
def tabela_cursos():
    banco, cursor = fg.acessar_banco(caminho_arquivo)
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS professor (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, descricao TEXT NOT NULL)")
        banco.commit()
        print('Tabela criada com sucesso!')
    except Exception as erro:
        print('Houve um erro ao criar a tabela.', erro)
    finally:
        banco.close()