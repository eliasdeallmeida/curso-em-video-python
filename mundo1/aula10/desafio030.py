# Aula 10 - Programa que recebe um número e informa se ele é par ou ímpar

print('========== DESAFIO 030 ==========')
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar.'.format(numero))