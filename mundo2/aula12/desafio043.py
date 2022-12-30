# Aula 12 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela: Abaixo de 18.5 (Abaio do peso); Entre 18.5 e 25 (Peso ideal); Entre 25 e 30 (Sobrepeso); Entre 30 e 40 (Obesidade); Acima de 40 (Obesidade mórbida).

from math import pow
print('========== DESAFIO 043 ==========')
print('Calculadora de IMC (Índice de Massa Corporal)')
peso = float(input('Seu peso (Kg): '))
altura = float(input('Sua altura (metros): '))
imc = peso / pow(altura, 2)
print('IMC: {:.1f} '.format(imc), end = '')
if imc < 18.5:
    print('(ABAIXO DO PESO)')
elif 18.5 <= imc < 25:
    print('(PESO NORMAL)')
elif 25 <= imc < 30:
    print('(SOBREPESO)')
elif 30 <= imc < 40:
    print('(OBESIDADE)')
else:
    print('(OBESIDADE MÓRBIDA)')