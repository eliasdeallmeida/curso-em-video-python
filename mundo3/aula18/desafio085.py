'''
DESAFIO 085 (AULA 18)
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

numeros = [[], []]
for n in range(1, 8):
    valor = int(input(f'{n}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares informados foram {numeros[0]}')
print(f'Os números ímpares informados foram {numeros[1]}')