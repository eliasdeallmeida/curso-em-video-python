# Aula 14 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('========== DESAFIO 065 ==========')
soma = 0
cont = 1
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número: '))
    if cont == 1:
        menor = maior = num
    else:
        if num > maior: maior = num
        elif num < menor: menor = num
    soma += num
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        cont += 1
    elif continuar == 'N':
        media = soma / cont
print('Você digitou {} números e a soma entre eles vale {}.'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))