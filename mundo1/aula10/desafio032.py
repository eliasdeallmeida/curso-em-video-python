# Aula 10 - Programa que lê um ano do usuário e informa se ele é bissexto ou não

from calendar import isleap
print('========== DESAFIO 032 ==========')
ano = int(input('Informe um ano: '))
if isleap(ano):
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))