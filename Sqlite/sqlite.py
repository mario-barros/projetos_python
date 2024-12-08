import sqlite3 as bd

'''
cursor.execute("INSERT INTO pessoas VALUES('Maria', 40, 'mario.barros@gmail.com')")

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
'''

#Função para acessar tabela
def acessar_banco():
    banco = bd.connect('usuarios.db')
    cursor = banco.cursor()
    return banco, cursor
#Função para criar tabela
def criar_tabela():
    banco, cursor = acessar_banco()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text, idade integer, email text)")
        banco.commit() #Atualiza o banco
        print('Tabela criada com sucesso!')
    except Exception as erro:
        print(f'Houve um erro na criação da tabela.', erro)
    finally:
        banco.close() # Fecha o banco

nome = str(input("Digite o nome: "))
idade = int(input("Digite a idade: "))
email = str(input("Digite o email: "))

#Função para adicionar valores ao banco
def adiciona_dados(nome, idade, email):
    banco, cursor = acessar_banco()
    try:
        cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES(?, ?, ?)", (nome, idade, email))
        banco.commit()
        print('Dados adicionados com sucesso!')
    except Exception as erro:
        print('Houve um erro ao adicionar dados ao banco de dados', erro)
    finally:
        banco.close()

criar_tabela()
adiciona_dados(nome, idade, email)
