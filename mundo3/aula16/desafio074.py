# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint
print('========== DESAFIO 074 ==========')
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números gerados foram {numeros}')
print(f'O menor foi {min(numeros)} e o maior foi {max(numeros)}')