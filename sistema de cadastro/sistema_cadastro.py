usuarios = []

#Menu
print('[1] Adicionar novo usuário\n[2] Listar todos os usuários\n[3] Actualizar informações de um usuário\n[4] Excluir um usuário\n[5] Sair do programa')

#Adicionar novo usuário
while True:
    opcao = int(input('\nEscolha uma opção: '))
    if opcao == 1:
        dict_user = {'Nome': input('\nDigite o seu nome: ').upper(), 
                    'Idade': int(input('Digite a sua idade: ')), 
                    'Email': input('Digite o seu email: ')}
        usuarios.append(dict_user)
        print('\nCADASTRO FEITO COM SUCESSO!')
    #Listar usuários
    elif opcao == 2:
        if not usuarios:
            print('\nNão existem usuários cadastrados!')
        else:
            print('\nDADOS DOS USUÁRIOS.\n')
            for u in usuarios:
                for c, v in u.items():
                    print(f'{c}: {v}')
    #Atualizar informações do usuário
    if opcao == 3:
        user = input('Informe o nome do usuário: ').upper()
