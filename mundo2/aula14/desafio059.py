# Aula 14 - Crie um programa que leia dois valores e mostre um menu na tela ([1] somar; [2] multiplicar; [3] maior; [4] novos números; [5] sair do programa). Seu programa deverá realizar a operação solicitada em cada caso.

print('========== DESAFIO 059 ==========')
print('Digite dois números')
num1 = int(input('\n1º número: '))
num2 = int(input('2º número: '))
sair = False
while not sair:
    print('-' * 18)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair')
    print('-' * 18)
    acao = int(input('-> O que deseja fazer? '))
    if acao == 1:
        resultado = num1 + num2
        print('A soma entre {} e {} vale {}.'.format(num1, num2, resultado))
    elif acao == 2:
        resultado = num1 * num2
        print('A multiplicação entre {} e {} vale {}.'.format(num1, num2, resultado))
    elif acao == 3:
        print('Entre {} e {}, o maior é '.format(num1, num2), end = '')
        if num1 > num2:
            resultado = num1
        elif num2 > num1:
            resultado = num2
        print('{}.'.format(resultado))
    elif acao == 4:
        num1 = int(input('\n1º número: '))
        num2 = int(input('2º número: '))
    elif acao == 5:
        sair = True
print('\nFim do programa.')