# Aula 07 - Programa que recebe a quantidade de km percorridos por um carro alugado e a quantidade de dias que ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

print('========== DESAFIO 015 ==========')
print('Aluguel de carro')
dias = int(input('Informe a quantidade de dias alugados: '))
distancia = int(input('Informe os quilômetros percorridos: '))
aluguel = dias * 60 + distancia * 0.15
print('O total a pagar é R$ {:.2f}'.format(aluguel))