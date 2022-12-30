'''
DESAFIO 088 (AULA 18)
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint

jogos = []
numeros = []

qtd_jogos = int(input('Quantos jogos deseja gerar? '))
for j in range(1, qtd_jogos + 1):
    cont = 1
    while True:
        valor = randint(1, 60)
        if valor not in numeros:
            numeros.append(valor)
            cont += 1
        if cont > 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')