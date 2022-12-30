# Aula 15 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('========== DESAFIO 068 ==========')
vitorias = 0
while True:
    numCmpt = randint(0, 10)
    numJgdr = int(input('Digite um número: '))
    pi = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    total = numCmpt + numJgdr
    print('-' * 55)
    print(f'Você jogou {numJgdr} e o computador jogou {numCmpt}. Resultado {total}: ', end = '')
    print('PAR.' if total % 2 == 0 else 'ÍMPAR.')
    if total % 2 == 0 and pi == 'P' or total % 2 != 0 and pi == 'I':
        print('VENCEU!')
        print('-' * 55)
        vitorias += 1
    else:
        print('PERDEU!')
        print('-' * 55)
        break
print(f'Você venceu {vitorias} vezes consecutivas.')