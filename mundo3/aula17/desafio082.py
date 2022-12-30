# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

print('========== DESAFIO 082 ==========')
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Os números digitados foram {lista}')
print(f'Os pares são {pares}')
print(f'Os ímpares são {impares}')