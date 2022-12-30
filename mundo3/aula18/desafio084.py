'''
DESAFIO 084 (AULA 18)
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

pessoas = []
dados = []
maior_peso = menor_peso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        elif dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break

print(f'Foram registradas {len(pessoas)} pessoas')
print(f'\nO maior peso foi {maior_peso} Kg, registrado por ', end = '')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'{p[0]} ', end = '')

print(f'\nO menor peso foi {menor_peso} Kg, registrado por ', end = '')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'{p[0]} ', end = '')