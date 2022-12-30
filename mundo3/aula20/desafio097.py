'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                      escreva('Olá, Mundo!') Saída:                                                                                                   ~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
'''

def escreveTextoFormatado(texto):
    espacoUnilateralDoTexto = 3
    tamanhoTexto = len(texto) + espacoUnilateralDoTexto * 2
    print('~' * tamanhoTexto)
    print(f'{" " * espacoUnilateralDoTexto}{texto}')
    print('~' * tamanhoTexto)


mensagem = str(input('Digite uma mensagem: '))
escreveTextoFormatado(mensagem)