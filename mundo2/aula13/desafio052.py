# Aula 13 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('========== DESAFIO 052 ==========')
print('Verificador de números primos')
num = int(input('Digite um número inteiro: '))
verifica = int(0)
for cont in range(1, num + 1):
    print('{}'.format(cont), end = ' ')
    if num % cont == 0: verifica += 1
    if verifica > 2: break
if verifica == 2: print('O número {} é primo!'.format(num))
else: print('O número {} NÃO é primo!'.format(num))