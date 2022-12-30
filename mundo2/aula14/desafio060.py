# Aula 14 - Faça um programa que leia um número qualquer e mostre o seu fatorial.

print('========== DESAFIO 060 ==========')
print('Calculadora de fatorial')
numero = int(input('Digite um número: '))
cont =  numero
fatorial = 1
while cont >= 1:
    fatorial *= cont
    cont -= 1
print('{}! = {}'.format(numero, fatorial))