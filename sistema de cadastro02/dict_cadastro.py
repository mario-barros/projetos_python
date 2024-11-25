#Função para o menú principal
def menu_principal():
    #while True:
        #Opções de menú
        print("1. Cadastrar Usuário\n2. Atualizar Usuário\n3. Remover Usuário\n4. Consultar Usuário\n5. Listar Usuário\n6. Exportar Dados\n7. Sair\n")

        #Escolher opção
        escolha = int(input("Escolha uma opção: "))

#Função para cadastro
def cadastrar_usuario(dados):
        dict_usuario = {'nome': input('Digite o nome: '),
                        'email': input('Digite o email: '),
                        'telefone': input('Digite o telefone'),
                        }
        dados.append(dict_usuario)