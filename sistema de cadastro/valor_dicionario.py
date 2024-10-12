def valor_procurado(lista, valor_proc):
    for dicionario in lista:
        for chave, valor in dicionario.items():
            if valor == valor_proc:
                return valor
            
def alterar_valor(lista2, chave_busca, valor_busca, chave_alterar, valor_alterar):
    for dicionario2 in lista2:
        if dicionario2.get(chave_busca) == valor_busca:
            dicionario2[chave_alterar] = valor_alterar
