# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sortearCincoValores(sorteio):
    print('O números sorteados foram: [', end = '')
    for cont in range(0, 5):
        sorteio.append(randint(0, 10))
        sleep(0.5)
        print(f' {sorteio[cont]} ', end = '', flush = True)
    print(']')

def somarValoresPares(numeros):
    somaValoresPares = 0
    print('Os números pares são: [', end = '')
    for numero in numeros:
        if numero % 2 == 0:
            somaValoresPares += numero
            sleep(0.5)
            print(f' {numero} ', end = '')
    print(']')
    print(f'A soma dos números pares vale {somaValoresPares}')

numeros = list()
sortearCincoValores(numeros)
somarValoresPares(numeros)