# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidades import moeda

valor = float(input('Informe um valor: R$ '))
taxaDeAumento = float(input('Informe a porcentagem da taxa de aumento: '))
taxaDeReducao = float(input('Informe a porcentagem da taxa de redução: '))
moeda.mostrarResumo(valor, taxaDeAumento, taxaDeReducao, formatar = True)