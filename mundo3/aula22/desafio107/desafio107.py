# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor = float(input('Informe um valor: R$ '))
taxa = float(input('Informe a porcentagem da taxa: '))

print(f'{" RESULTADOS DOS CÁLCULOS ":=^50}')
print(f'O aumento de {taxa}% de {valor} vale {moeda.calcularAumentoDoValor(valor, taxa):.2f}')
print(f'A redução de {taxa}% de {valor} vale {moeda.calcularReducaoDoValor(valor, taxa):.2f}')
print(f'O dobro de {valor} é {moeda.calcularDobroDoValor(valor):.2f}')
print(f'A metade de {valor} é {moeda.calcularMetadeDoValor(valor):.2f}')