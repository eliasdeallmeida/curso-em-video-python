# Aula 10 - Programa que lê 3 número e informa qual é o maior e o menor

print('========== DESAFIO 033 ==========')
print('Digite 3 números e eu direi qual é maior e qual é menor.')
num1 = int(input('1º número: '))
num2 = int(input('2º número: '))
num3 = int(input('3º número: '))
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print('Dentre {}, {} e {} o menor é {} e o maior é {}'.format(num1, num2, num3, menor, maior))