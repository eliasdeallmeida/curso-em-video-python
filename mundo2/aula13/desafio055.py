# Aula 13 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('========== DESAFIO 055 ==========')
print('Informe o peso de 5 pessoas')
for cont in range(1, 5 + 1):
    peso = float(input('{}ª pessoa: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    if peso > maior: maior = peso
    elif peso < menor: menor = peso
print('O maior peso informado foi {:.1f} Kg e o menor foi {:.1f} Kg.'.format(maior, menor))