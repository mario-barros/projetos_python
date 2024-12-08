import sqlite3 as sq
import os
'''
#Obtem o caminho do diretorio atual
diretorio_actual = os.path.dirname(__file__)
#Obtem o caminho do diretorio que contem o arquivo 
caminho_arquivo = os.path.join(diretorio_actual, '../banco_dados', 'primeiro_banco.db')'''
#Função para acessar ou criar o banco de dados
def acessar_banco(caminho):
    banco = sq.connect(caminho)
    cursor = banco.cursor()
    return banco, cursor
