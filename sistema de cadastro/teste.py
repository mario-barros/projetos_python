usuarios = []

dict_user = {'nome': input('\nDigite o seu nome: '), 
             'idade': int(input('Digite a sua idade: ')), 
             'email': input('Digite o seu email: ')}
usuarios.append(dict_user)

for u in usuarios:
    for k, v in u.items():
        print('\n', k, v)
