# Aula 07 - Programa que recebe o preço de um produto e mostra seu novo valor com 5% de desconto

print('========== DESAFIO 012 ==========')
print('Calculadora de desconto')
preco = float(input('Informe o valor do produto: '))
novoPreco = preco - (5/100 * preco)
print('O valor do produto com 5% de desconto vale R$ {:.2f}'.format(novoPreco))