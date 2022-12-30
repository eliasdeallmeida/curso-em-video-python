# Aula 08 - Programa que recebe um número real do teclado e mostre na tela sua porção inteira

from math import trunc
print('========== DESAFIO 016 ==========')
num = float(input('Digite um número real: '))
print('A parte inteira de {} é {}'.format(num, trunc(num)))