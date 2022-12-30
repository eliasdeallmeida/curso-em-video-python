# Aula 07 - Programa que recebe uma quantia de dinheiro em reais e mostre seu valor convertido em dólares (considere U$ 1,00 = R$ 3,27)

print('========== DESAFIO 010 ==========')
print('Conversor de real para dólar')
real = float(input('Informe uma quantia: '))
dolar = real / 5.18
print('Com R$ {:.2f} você pode comprar U$ {:.2f}'.format(real, dolar))