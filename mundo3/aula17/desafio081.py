# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados; B) A lista de valores, ordenada de forma decrescente; C) Se o valor 5 foi digitado e está ou não na lista.

print('========== DESAFIO 081 ==========')
lista = []
d5 = 0
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse = True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')