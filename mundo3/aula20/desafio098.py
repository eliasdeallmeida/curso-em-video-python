'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

from time import sleep

def fazerContagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if (passo < 0) ^ (inicio > fim):
        passo *= -1
    print('-' * 50)
    print(f'Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    sleep(1)
    print('[', end = '')
    numero = inicio
    if inicio == fim:
        print(f' {numero} ', end = '', flush = True)
    while (inicio < fim and numero <= fim) or (inicio > fim and numero >= fim):
        sleep(0.5)
        print(f' {numero} ', end = '', flush = True)
        numero += passo
    print(']')

# fazerContagem(1, 10, 1)
# fazerContagem(10, 0, 2)
print('-' * 50)
print('Sua vez de informar os dados da contagem!')
inicioContagem = int(input('-> Início: '))
fimContagem = int(input('-> Fim: '))
passoContagem = int(input('-> Passo: '))
fazerContagem(inicioContagem, fimContagem, passoContagem)