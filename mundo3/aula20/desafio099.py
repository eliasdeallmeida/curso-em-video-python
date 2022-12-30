# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def analisarMaiorValor(*numeros):
    print('-' * 50)
    print(f'Números informados: [', end = '')
    maior = numeros[0]
    for num in numeros:
        sleep(0.5)
        print(f' {num} ', end = '', flush = True)
        if num > maior:
            maior = num
    print(']')
    print(f'Foram informados {len(numeros)} números e o maior deles é o {maior}')

analisarMaiorValor(4, 3, 1, 5)
analisarMaiorValor(1, -12, 10, -3, 7)
analisarMaiorValor(42, 27, 88, 23, 14, 74)