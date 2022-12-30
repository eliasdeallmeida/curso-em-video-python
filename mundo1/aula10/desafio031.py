# Aula 10 - Programa que pergunta a distância de uma viagem em quilômetros e calcula o preço da passagem cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas

print('========== DESAFIO 031 ==========')
distancia = int(input('Informe a distância da viagem (km): '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('O preço para uma viagem de {} km é de R$ {:.2f}'.format(distancia, preco))