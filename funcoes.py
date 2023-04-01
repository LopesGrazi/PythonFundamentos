# 1. O que são funcções e por que utilizá-las?

# Funções que já utilizamos anteriormente...

'''print() # - Imprime uma mensage (int, float,str)no console(terminal,cmd)
input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len() # - Recebe uma lista e retorna o tamanho dessa lista
max() # - Retorna o maior valor de uma lista'''

# 2. Criação de funções

#Função inicial

def saudacao():
    print('Seja bem-vindo(a)!')
    print('É um prazer ter você fazendo parte desse curso.')

saudacao()

#Função com parâmetro

def saudacao(nome, curso):
    print(f'Seja bem-vindo(a)!', (nome))
    print(f'É um prazer ter você fazendo parte do curso de', (curso))
saudacao('Juninho', 'PowerBI')

#Funções com parâmetro default

def saudacao(nome, curso ='Python'):
    print(f'Seja bem-vindo(a)!', (nome))
    print(f'É um prazer ter você fazendo parte do curso de',(curso))
saudacao('Grazi')

#Funções com Retorno

def soma(num1, num2):
    print('O resultado da soma é', num1 + num2)
soma(5, 7)
    
def soma(num1, num2):
    return num1 + num2
resultado = soma(5,7)
print('O resultado da soma é', resultado)

def calculadora(num1, num2, operacao = '+'):
    if operacao == '+':
        return num1+num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(90,20,'-')
print(resultado)