ano_atual = 2024
ids_atuais = [("20240001",), ("20240002",), ("20240003",)]
ultimo_id = max([(id[0][4:]) for id in ids_atuais])
#novo_numero = ultimo_id + 1
#id_unico = f"{ano_atual}{novo_numero:04d}"
print(ultimo_id)
