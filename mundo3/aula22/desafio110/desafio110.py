# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

valor = float(input('Informe um valor: R$ '))
taxa = float(input('Informe a porcentagem da taxa: '))
moeda.mostrarResumo(valor, taxa, formatar = True)