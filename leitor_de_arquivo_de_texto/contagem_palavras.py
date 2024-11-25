import os

caminho = os.path.join(os.path.dirname(__file__), 'arquivos', 'arq.txt')

with open (caminho, 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    contador = 0
    for i in palavras:
        contador += 1
    print(f"O arquivo contem {contador} palavras.")