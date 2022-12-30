# Aula 12 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: Se ele ainda vai se alistar ao serviço miliar; Se é a hora de se alistar; Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('========== DESAFIO 039 ==========')
print('Veremos se você precisa se alistar no exército.')
anoNasc = int(input('Por favor, informe seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print('Quem nasceu em {} tem {} anos de idade em {}'.format(anoNasc, idade, anoAtual))
if idade == 18:
    print('É hora de se alistar no exército!')
elif idade < 18:
    tempo = 18 - idade
    if tempo == 1:
        print('Ainda falta {} ano para você se alistar no exército!'.format(tempo))
    else:
        print('Ainda faltam {} anos para você se alistar no exército!'.format(tempo))
    anoAlst = anoAtual + tempo
    print('Seu alistamento será em {}'.format(anoAlst))
else:
    tempo = idade - 18
    if tempo == 1:
        print('Já passou {} ano desde o seu tempo de alistamento!'.format(tempo))
    else:
        print('Já passaram {} anos desde o seu tempo de alistamento!'.format(tempo))
    anoAlst = anoAtual - tempo
    print('Seu alistamento deveria ter acontecido em {}'.format(anoAlst))