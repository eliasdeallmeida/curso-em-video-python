# Aula 13 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('========== DESAFIO 051 ==========')
print('Calculadora de Progressão Aritmética')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
enesimo = primeiro + (10 - 1) * razao
for cont in range(primeiro, enesimo+razao, razao):
    print('{}'.format(cont), end = ' -> ')
print('FIM')