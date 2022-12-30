# Aula 10 - Programa que lê a velocidade de um carro. Se ultrapassar 80 km/h imprima uma mensagem dizendo que ele foi multado, na qual a multa custará R$ 7,00 por cada km acima do limite.

print('========== DESAFIO 029 ==========')
velocidade = int(input('Informe a velocidade média (km/h): '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você deverá pagar uma multa de R$ {:.2f}'.format(multa))
print('Dirija com cuidado! Tenha um bom dia!')