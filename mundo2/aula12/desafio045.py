# Aula 12 - Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('========== DESAFIO 045 ==========')
print('Bem vindo ao jogo de Jokenpô!')
print('Digite "sair" para encerrar o jogo.')
print('''(1) Pedra
(2) Papel
(3) Tesoura''')
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
while 1:
    jogadaCmpt = randint(1, 3)
    jogadaPlyr = str(input('\nSua jogada: '))
    if jogadaPlyr == 'sair':
        print('Obrigado por jogar!')
        break
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    jogadaPlyr = int(jogadaPlyr)
    print('-=' * 13)
    print('O Computador jogou {}'.format(opcoes[jogadaCmpt - 1]))
    print('Você jogou {}'.format(opcoes[jogadaPlyr - 1]))
    print('-=' * 13)
    if jogadaPlyr == jogadaCmpt:
        print('EMPATE!')
    elif jogadaPlyr == 1 and jogadaCmpt == 3 or jogadaPlyr == 2 and jogadaCmpt == 1 or jogadaPlyr == 3 and jogadaCmpt == 2:
        print('Você VENCEU!')
    else:
        print('Você PERDEU!')