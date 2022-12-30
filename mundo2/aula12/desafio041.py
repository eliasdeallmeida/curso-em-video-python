# Aula 12 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos (MIRIM); Até 14 anos (INFANTIL); Até 19 anos (JUNIOR); Até 25 anos (SÊNIOR); Acima (MASTER)

from datetime import date
print('========== DESAFIO 041 ==========')
print('Veremos em qual categoria de natação você se adequa.')
anoNasc = int(input('Por favor, digite seu ano nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print('Você tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('Categoria MIRIM.')
elif 9 < idade <= 14:
    print('Categoria INFANTIL.')
elif 14 < idade <= 19:
    print('Categoria JUNIOR')
elif 19 < idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')