'''
DESAFIO 087 (AULA 18)
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna3 = maior_valor_linha2 = 0

print('Preencha a matriz')
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'valor[{linha + 1}][{coluna + 1}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

for linha in range(0, 3):
    soma_coluna3 += matriz[linha][2]

for coluna in range(0, 3):
    if matriz[1][coluna] > maior_valor_linha2:
        maior_valor_linha2 = matriz[1][coluna]

print('Matriz Informada')
for linha in range(0, 3):
    print('|', end = '')
    for coluna in range(0, 3):
        print(f' {matriz[linha][coluna]} ', end = '')
    print('|')

print(f'A soma dos pares informados vale {soma_pares}')
print(f'A soma dos elementos da coluna 3 vale {soma_coluna3}')
print(f'O maior valor da linha 2 é {maior_valor_linha2}')