# Aula 13 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
print('========== DESAFIO 054 ==========')
anoAtual = date.today().year
maiorDeIdade = int(0)
print('Informe o ano de nascimento de 7 pessoas')
for cont in range(1, 7 + 1):
    anoNasc = int(input('{}ª pessoa: '.format(cont)))
    if anoAtual - anoNasc >= 21:
        maiorDeIdade += 1
print('De 7 pessoas, {} atingiram a maioridade e {} não.'.format(maiorDeIdade, 7 - maiorDeIdade))
    