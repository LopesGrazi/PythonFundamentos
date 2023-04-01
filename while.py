numero_sorteado = 15
numero_escolhido = int(input('Escolha um número de 0 a 20:'))

while numero_sorteado != numero_escolhido:
    print('Você errou, tente novamente...')
    numero_escolhido = int(input('Escolha um número de 1 a 20:'))
print('Parabéns, você acertou!')

contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
