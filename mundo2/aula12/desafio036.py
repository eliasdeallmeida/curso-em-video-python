# Aula 12 - Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. É necessário perguntar o valor da casa, o valor do salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('========== DESAFIO 036 ==========')
valorCasa = float(input('Valor da casa: R$ '))
salario = float(input('Seu salário: R$ '))
anos = int(input('Em quantos meses deseja pagar? '))
prestacao = valorCasa / (anos * 12)
limite = (30/100) * salario
print('A prestação mensal é R$ {:.2f} e o limite do salário é R$ {:.2f}.'.format(prestacao, limite))
if prestacao <= limite:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')