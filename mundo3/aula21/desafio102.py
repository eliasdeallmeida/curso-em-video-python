# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def calcularFatorial(numero, mostrarCalculo = False):
    fatorial = 1
    print(f'{numero}! = ', end = '')
    for num in range(numero, 0, -1):
        fatorial *= num
        if mostrarCalculo:
            print(num, end = '')
            if num > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
    return fatorial

print(f'{"CALCULADORA DE FATORIAL":^50}')
numero = int(input('Informe um número: '))
print(calcularFatorial(numero, mostrarCalculo = True))