import os

print('ESCREVA O TEXTO A BAIXO.')
usuario = input("")
caminho = os.path.join(os.path.dirname(__file__), 'arquivos', 'arq3.txt')

with open(caminho, 'a') as arquivo:
    conteudo = arquivo.write(usuario + '\n')

with open(caminho, 'r') as arquivo_leitura:
    conteudo_leitura = arquivo_leitura.read()
    print('')
    print(conteudo_leitura)
