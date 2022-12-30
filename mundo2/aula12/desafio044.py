# Aula 12 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: À vista dinheiro/cheque (10% de desconto); à vista no cartão (5% de desconto); Em até 2x no cartão (preço normal); 3x ou mais no cartão (20% de juros)

print('========== DESAFIO 044 ==========')
valor = float(input('Valor do produto: R$ '))
print('------------------------')
print('(1) À vista em dinheiro')
print('(2) À vista em cheque')
print('(3) À vista no cartão')
print('(4) Parcelado no cartão')
print('------------------------')
pag = int(input('Escolha a forma de pagamento: '))
if pag == 1 or pag == 2:
    valor = valor - (10/100 * valor)
elif pag == 3:
    valor = valor - (5/100 * valor)
elif pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas > 2:
        valor = valor + (20/100 * valor)
    valorParcela = valor / parcelas
    print('Sua compra foi parcelada em {}x e cada parcela custa R$ {:.2f}.'.format(parcelas, valorParcela))
else:
    print('Forma de pagamento não reconhecida!')
print('O preço do produto é R$ {:.2f}'.format(valor))