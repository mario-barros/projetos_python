from random import randint

while True:
    usuario = input("\nRODAR O DADO [Sim/Não]: ")
    opcao = usuario[0].lower()
    if opcao == 's':
        rodar = randint(1, 6)
        print('\nO RESULTADO É: ', rodar)
    else:
        print('\nOK, PROGRAMA ENCERRADO!')    
        break
