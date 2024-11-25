import os

# Limpa o terminal quando executado
if os.name == 'nt':
    _ = os.system('cls')
else:
    _ = os.system('clear')
def leitor():

    # Cria o caminho relativo em relação a localização do script
    # Define o arquivo a ser lido
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'arquivos', 'arq.txt')

    # Tentando abrir o aqruivo
    if os.path.exists(caminho_arquivo):
        # Lê e exibe o conteúdo do arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    else:
        # Caso o arquivo não for encontrado
        print("ERRO: arquivo não encontrado!")

if __name__ == "__main__":
    leitor()
