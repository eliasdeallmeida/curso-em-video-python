# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

ranking = []
jogadas = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

print('-=' * 15)
print(f'{"JOGADAS":^30}')
for jogador, valor in jogadas.items():
    sleep(1)
    print(f'{jogador} tirou {valor} no dado')

ranking = sorted(jogadas, key = jogadas.get, reverse = True)

print('-=' * 15)
print(f'{"RANKING":^30}')
for posicao, jogador in enumerate(ranking):
    sleep(1)
    print(f'{posicao + 1}º lugar: {jogador} ({jogadas[jogador]} pts)')

print('-=' * 15)