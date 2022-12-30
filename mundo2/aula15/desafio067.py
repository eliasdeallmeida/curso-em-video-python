# Aula 15 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('========== DESAFIO 067 ==========')
print('Calculadora de tabuada (Digite um número negativo para parar)')
while True:
    num = int(input('\nDigite um número: '))
    if num < 0:
        break
    cont = 1
    print('-' * 12)
    while cont <= 10:
        print(f'{num} x {cont:2} = {num * cont}')
        cont += 1
    print('-' * 12)
print('\nFIM')