# Aula 07 - Programa que recebe um número inteiro e mostra sua tabuada

print('========== DESAFIO 009 ==========')
print('Calculadora de tabuada (1 a 10)')
num = int(input('Digite um número: '))
print('-' * 12)
for tabuada in range (10):
    tabuada = tabuada + 1
    result = num * tabuada
    print('{} x {:2} = {}'.format(num, tabuada, result))
print('-' * 12)