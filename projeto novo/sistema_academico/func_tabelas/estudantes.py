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
caminho_arquivo = os.path.join(diretorio_actual, '../banco_dados', 'estudantes.db')

fg.acessar_banco(caminho_arquivo)
#Função para criar tabela dos estudantes
def tabela_estudantes():
    banco, cursor = fg.acessar_banco(caminho_arquivo)
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS estudantes (id INTEGER, nome TEXT NOT NULL, data_nascimento TEXT NOT NULL, localidade TEXT NOT NULL)")
        banco.commit()
        print("Tabela criada com sucesso!")
    except Exception as erro:
        print("Houve um problema ao criar a tabela.", erro)
    finally:
        banco.close()