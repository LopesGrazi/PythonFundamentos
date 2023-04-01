soma = 0

for i in range(1,4):
    nota = float(input(f'Informe sua nota {i}: '))
    soma = soma + nota

print('Sua média é: ') 
print(soma / 3)