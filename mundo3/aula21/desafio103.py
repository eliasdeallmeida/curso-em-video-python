# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def mostrarFichaJogador(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} marcou {gols} gols')

nomeJogador = str(input('Nome do jogador: ')).strip().title()
golsFeitos = str(input('Gols feitos: ')).strip()
if golsFeitos.isnumeric():
    golsFeitos = int(golsFeitos)
else:
    golsFeitos = 0
if nomeJogador == '':
    mostrarFichaJogador(gols = golsFeitos)
else:
    mostrarFichaJogador(nomeJogador, golsFeitos)