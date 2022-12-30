# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

valor = float(input('Informe um valor: R$ '))
taxa = float(input('Informe a porcentagem da taxa: '))

print(f'{" RESULTADOS DOS CÁLCULOS ":=^50}')
print(f'O aumento de {taxa}% de {moeda.formatarValorMonetario(valor)} vale {moeda.calcularAumentoDoValor(valor, taxa, True)}')
print(f'A redução de {taxa}% de {moeda.formatarValorMonetario(valor)} vale {moeda.calcularReducaoDoValor(valor, taxa, True)}')
print(f'O dobro de {moeda.formatarValorMonetario(valor)} é {moeda.calcularDobroDoValor(valor, True)}')
print(f'A metade de {moeda.formatarValorMonetario(valor)} é {moeda.calcularMetadeDoValor(valor, True)}')