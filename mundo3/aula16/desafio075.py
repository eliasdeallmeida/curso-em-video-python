# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9; B) Em que posição foi digitado o primeiro valor 3; C) Quais foram os números pares.

print('========== DESAFIO 075 ==========')
numeros = (int(input('Primeiro número: ')), int(input('Segundo número: ')), int(input('Terceiro número: ')), int(input('Quarto número: ')))
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 apareceu primeiro na posição {numeros.index(3)+1}.')
else:
    print('O número 3 não foi encontrado.')
print('Os números pares são ', end = '')
for i in numeros:
    if i % 2 == 0:
        print(i, end = '')