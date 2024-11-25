import os


palavra = input("Digite a palavra que deseja procurar: ").lower()
caminho = os.path.join(os.path.dirname(__file__), 'arquivos', 'arq3.txt')

contador = 0
existe = False
with open(caminho, 'r') as arquivo:
    conteudo = arquivo.read().lower()
    palavras = conteudo.split()
    for p in palavras:
        if palavra == p:
            existe = True
            contador += 1
    if existe == True:
        print(f"A palavra \"{palavra}\" existe no arquivo e foi encontrada {contador} vez(es).")
    else:
        print(f"A palavra \"{palavra}\" não foi encontrada no arquivo.")
