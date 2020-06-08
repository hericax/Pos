# criando o discionário
inventario = {'kiwis': 430, 'bananas': 525, 'laranjas': 525, 'peras': 217}
#print(inventario)

# incluir um item ao dicionário
inventario['amora'] = '500'
#print(inventario)

#pesquisar no dicionário por chave
value = inventario['laranjas']
#print(value)


# Remoção de um par chave-valor do dicionário
del inventario['peras']
#print(inventario)


# incluindo abacaxi
inventario['abacaxi'] = ' 0 '
#print ("inclusão do abacaxi", inventario)

# recuperando
fruta = inventario['abacaxi'] = 0
#print ('recuperação da fruta: ', fruta)

# atualizando o valor das bananas
inventario['bananas'] = inventario['bananas'] + 200
#print (inventario)
numItems = len(inventario)
#print (numItems)


# método keys - Retorna uma vista(view) das chaves no dicionário.  Podemos iterar sobre a vista ou transformar a vista em uma lista usando a função list de conversão.
# opção 1 de uso do keys
for akey in inventario.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventario[akey])

ks = list(inventario.keys())
print(ks)

for k in inventario:
   print("Got key", k)


# opção 2 de uso do keys
for k in inventario:
   print("Got key", k)

# Note que os tuplas são muitas vezes úteis para obter tanto a chave quanto o valor ao mesmo tempo, enquanto você está iterando no laço. Os dois laços fazer a mesma coisa.
#Os operadores in e not in podem testar se uma chave está no dicionário:
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")