'''
DESAFIO 089 (AULA 18)
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

boletim = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer informar mais dados? ')).upper()[0]
    if continuar == 'N':
        break

print('-' * 30)
print(f'{"Nº":<4}{"NOME":<20}{"MÉDIA":>6}')
print('-' * 30)
for cont, dados in enumerate(boletim):
    print(f'{cont:<4}{dados[0]:<20}{dados[2]:>6.1f}')
print('-' * 30)

while True:
    aluno = int(input('Informe o número do(a) aluno(a) [-1 para sair]: '))
    if aluno == -1:
        break
    print(f'{boletim[aluno][0]} tirou as notas {boletim[aluno][1]}')