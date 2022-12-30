# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

valor = float(input('Informe um valor: R$ '))
taxa = float(input('Informe a porcentagem da taxa: '))

print(f'{" RESULTADOS DOS CÁLCULOS ":=^50}')
print(f'O aumento de {taxa}% de {moeda.formatarValorMonetario(valor)} vale {moeda.formatarValorMonetario(moeda.calcularAumentoDoValor(valor, taxa))}')
print(f'A redução de {taxa}% de {moeda.formatarValorMonetario(valor)} vale {moeda.formatarValorMonetario(moeda.calcularReducaoDoValor(valor, taxa))}')
print(f'O dobro de {moeda.formatarValorMonetario(valor)} é {moeda.formatarValorMonetario(moeda.calcularDobroDoValor(valor))}')
print(f'A metade de {moeda.formatarValorMonetario(valor)} é {moeda.formatarValorMonetario(moeda.calcularMetadeDoValor(valor))}')