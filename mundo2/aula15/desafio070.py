# Aula 15 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: (A) qual é o total gasto na compra; (B) quantos produtos custam mais de R$1000; (C) qual é o nome do produto mais barato.

print('========== DESAFIO 070 ==========')
custoTotal = pMil = cont = 0
while True:
    print('-' * 35)
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço do produto: R$ '))
    print('-' * 35)
    cont += 1
    custoTotal += preco
    if preco > 1000.00:
        pMil += 1
    if cont == 1 or preco < precoMB:
        precoMB = preco
        nomeMB = nome
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar != 'S':
        break
print(f'\nCusto total da compra: R$ {custoTotal:.2f}')
print(f'Quantidade produtos que custam menos de R$ 1000,00: {pMil}')
print(f'Nome do produto mais barato: {nomeMB}')