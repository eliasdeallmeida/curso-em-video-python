# Aula 14 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('========== DESAFIO 064 ==========')
print('Somador de números (Digite 999 para parar)')
cont = 1
soma = 0
parar = False
while not parar:
    num = int(input('{}º número: '.format(cont)))
    if num != 999:
        soma += num
        cont += 1
    else:
        cont -= 1
        parar = True
print('Foram digitados {} números e a soma sentre eles é {}.'.format(cont, soma))