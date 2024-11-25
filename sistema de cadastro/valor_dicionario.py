def valor_procurado(lista, valor_proc):
    for dicionario in lista:
        for chave, valor in dicionario.items():
            if valor == valor_proc:
                return valor
            
def alterar_valor(lista2, chave_busca, valor_busca, chave_alterar, valor_alterar):
    for dicionario2 in lista2:
        if dicionario2.get(chave_busca) == valor_busca:
            dicionario2[chave_alterar] = valor_alterar

def excluir_usuario(lista3, chave_busca2, valor_busca2):
    for indice, dicionario3 in enumerate(lista3):
        if dicionario3[chave_busca2] == valor_busca2:
            del lista3[indice]
