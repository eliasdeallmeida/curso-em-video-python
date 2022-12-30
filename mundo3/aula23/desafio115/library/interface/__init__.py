from library.input import *

def imprimirLinha(tamanho = 50, caractere = '-'):
    print(caractere * tamanho)

def mostrarTextoFormatado(texto = ''):
    tamanhoTotal = 50
    imprimirLinha(tamanhoTotal)
    print(texto.center(tamanhoTotal))
    imprimirLinha(tamanhoTotal)

def menu(lista):
    mostrarTextoFormatado('MENU DE SELEÇÃO')
    for numeracao, item in enumerate(lista):
        print(f'{numeracao + 1} - {item}')
    imprimirLinha()
    return lerValorInteiro('Sua opção: ')