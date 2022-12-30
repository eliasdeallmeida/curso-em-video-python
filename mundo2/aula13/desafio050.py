# Aula 13 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('========== DESAFIO 050 ==========')
print('Digite 6 números')
soma = int(0)
for cont in range(1, 6+1):
    num = int(input('{}º número: '.format(cont)))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares digitados vale {}.'.format(soma))