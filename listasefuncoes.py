# > LISTAS: permitem diferentes tipos de dados
# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2


# Com lista
notas = [7.9 , 9.7 , 8.2]


# Criando listas
lista = [] #lista vazia
lista = list() #lista vazia
lista = [ 35 , 'Graziele', 3.1415, True ]
lista_de_listas = [10, [1,2,3]]

# Indexação e slices(fatiamento)
lista = [10, 'Graziele', 3.1415 , True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#Slices
lista = [10,50,30,40,25,60,5]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# > Interações com o FOR
# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices
# len vem de length(comprimento)

print('Comprimento da lista: ', len(lista))
 
for i in range(len(lista)):
    print(lista[i])

#Métodos de listas

lista = [1, 3, 12, 8, 2]

#append .adiciona um elemento ao final da lista
print('Antes do append:', lista)

lista.append(3)
print('Depois do append:', lista)

#Insert .adiciona um elemento no índice(posição) escolhida
lista.insert(2, 10)
print('Depois do insert:', lista)

# Extend  .junta duas listas, adiciona os elementos da nova lista no final da lista original
lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend:',  lista)

#Pop .remove um elemento específico, senão, o último elemento
lista.pop()
print('Depois do pop:', lista)
lista.pop(0)
print('Depois do pop:', lista)

#Remove  .remove o PRIMEIRO elemento (valor) específico(não é pelo índice)
lista.remove(3)
print('Depois do remove:', lista)

#Count .conta a quantidade de elementos iguais tem na lista
print ('Quantidade de 2 na lista:', lista.count(2))

#Index .diz qual é o índice do elemento
print('índice do elemento 12:', lista.index(12))

#Sort .ordena a lista 
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#Funções para Listas

#Len
print('Quantidade de elementos na lista:', len(lista))

#Sum
print('Soma dos elementos da lista:', sum(lista))

#Min
print('Menor elemento da lista:', min(lista))

#Max
print('Maior elemento da lista:', max(lista))
