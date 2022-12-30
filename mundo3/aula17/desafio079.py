# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('========== DESAFIO 079 ==========')
lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor já existe!')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print(f'Você digitou os números {lista}')