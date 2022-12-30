# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = list()
dados = dict()
gols = list()

while True:
    dados['Nome'] = str(input('Nome: ')).title()

    while True:
        qtd_partidas = int(input('Quantidade de partidas: '))
        if qtd_partidas >= 0:
            break
        print('>>> ERRO: Digite uma quantidade maior ou igual a zero.')

    for cont in range(0, qtd_partidas):
        while True:
            gols.append(int(input(f'Gols feitos na {cont + 1}ª partida: ')))
            if gols[cont] >= 0:
                break
            print('>>> ERRO: Digite uma quantidade maior ou igual a zero.')

    dados['Gols'] = gols[:]
    dados['Total de gols'] = sum(gols)
    jogadores.append(dados.copy())
    dados.clear()
    gols.clear()

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('>>> ERRO: Digite S para SIM ou N para NÃO.')

    if continuar == 'N':
        break

print('-=' * 25)
print(f'{"Nº":<5}{"Nome":<15}{"GOLS":<15}{"TOTAL DE GOLS":<15}')
print('-' * 50)

for numero, informacoes in enumerate(jogadores):
    print(f'{numero:<5}', end = '')
    for i in informacoes.values():
        print(f'{str(i):<15}', end = '')
    print()

print('-=' * 25)