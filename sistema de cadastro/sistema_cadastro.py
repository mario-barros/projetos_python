from valor_dicionario import valor_procurado, alterar_valor, excluir_usuario
usuarios = []

#Menu
print('[1] Adicionar novo usuário\n[2] Listar todos os usuários\n[3] Actualizar informações de um usuário\n[4] Excluir um usuário\n[5] Sair do programa')

while True:
    opcao = int(input('\nEscolha uma opção: '))
    #Adicionar novo usuário
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
        user = input('\nInforme o nome do usuário: ').upper()
        nome_do_usuario = valor_procurado(usuarios, user)
        if nome_do_usuario == user:
            print(f'\nO usuário {nome_do_usuario} está cadastrado.')
            print('\nQual é a informação que pretende alterar?\n[1] Nome.\n[2] Idade\n[3] Email')
            opcao_atualizar = int(input('Escolha uma opção: '))
            if opcao_atualizar == 1:
                novo_nome = input('Digite o novo nome: ')
                alterar_valor(usuarios, 'Nome', user, 'Nome', novo_nome)
                print('Nome atualizado: ', novo_nome)
            elif opcao_atualizar == 2:
                nova_idade = int(input('Digite a nova idade: '))
                alterar_valor(usuarios, 'Nome', user, 'Idade', nova_idade)
                print('Idade atualizada: ', nova_idade)
            elif opcao_atualizar == 3:
                novo_email = input('Digite o novo email: ')
                alterar_valor(usuarios, 'Nome', user, 'Email', novo_email)
                print('Novo email: ', novo_email)
        else:
            print('Usuário não encontrado.')
    #Excluir usuário
    if opcao == 4:
        user = input('Informe o nome do usuário: ').upper()
        nome_do_usuario = valor_procurado(usuarios, user)
        if nome_do_usuario == user:
            excluir_usuario(usuarios, 'Nome', user)
            print('Usuário excluido com sucesso!')
        else:
            print('Usuário não encontrado.')
    #Encerrar o programa
    if opcao == 5:
        print('\nPrograma Encerrado.')
        break
