# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()

jogador['Nome'] = str(input('Nome do jogador: '))
qtd = int(input('Quantidade de partidas jogadas: '))

for cont in range(0, qtd):
    gols.append(int(input(f'Gols feitos na {cont + 1}ª partida: ')))

jogador['Gols'] = gols[:]
jogador['Total de gols'] = sum(gols)

print('-=' * 25)
print(f'O jogador {jogador["Nome"]} participou de {len(jogador["Gols"])} jogos')

for partida, gols in enumerate(jogador['Gols']):
    print(f'Partida {partida + 1:<10}{gols:>10}')

print(f'Total de gols: {jogador["Total de gols"]}')
print('-=' * 25)