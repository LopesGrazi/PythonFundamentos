# condicionais: if and else

idade = 18
if idade >= 18:
    print('Você é maior de idade.')
else: 
    print('Você é menor de idade.')

media = float(input('Informe a média do estudante:'))
presenca = int(input('Informe o percentual de presenca do estudante:'))
if media >= 7 and presenca >= 70:
    print('Parabéns, você foi aprovado(a)!')
elif media >= 5 and presenca >= 50:
    print('Você está em recuparação.')
else:
    print('Você foi reprovado(a)!')