#Dicionários

#Criando dicionários

dicionario = {}
dicionario = dict ()

dicionario = {'nome': 'Grazi', 'idade': 35, 'altura':1.74}
print(dicionario['idade'])
print(dicionario)

#Adicionando elementos em um dicionário

dicionario['Analista de Dados'] = True
print(dicionario)

dicionario['altura'] = 1.75
print(dicionario)

#Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)