# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print('========== DESAFIO 078 ==========')
numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite o {c+1}º número: ')))
    if c == 0:
        maior = menor = numeros[0]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        elif numeros[c] < menor:
            menor = numeros[c]
print(f'\nO maior número foi {maior} e está localizado nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i+1} ', end='')
print(f'\nO menor número foi {menor} e está localizado nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i+1} ', end='')