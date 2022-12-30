# Aula 12 - Escreva um programa que leia um número inteiro qualquer e peça para que o usuário escolha qual será a base de conversão (1 para binário, 2 para octal, 3 para hexadecimal).

print('========== DESAFIO 037 ==========')
print('Conversor de bases numéricas')
decimal = int(input('Digite um número inteiro: '))
print('----------------')
print('(1) Binário')
print('(2) Octal')
print('(3) Hexadecimal')
print('----------------')
base = int(input('Para qual base deseja converter? '))
print('{} em base decimal = '.format(decimal), end = '')
if base == 1:
    print('{} em base binária.'.format(bin(decimal)[2:]))
elif base == 2:
    print('{} em base octal.'.format(oct(decimal)[2:]))
elif base == 3:
    print('{} em base hexadecimal.'.format(hex(decimal)[2:].upper()))
else:
    print('Base numérica inválida!')

"""
numero = decimal
if base == 1:
    binario = ''
    while numero > 0:
        binario += str(numero % 2)
        numero //= 2
    print('{} em base decimal = {} em base binária.'.format(decimal, binario[::-1]))
elif base == 2:
    octal = ''
    while numero > 0:
        octal += str(numero % 8)
        numero //= 8
    print('{} em base decimal = {} em base octal.'.format(decimal, octal[::-1]))
elif base == 3:
    hexadecimal = ''
    while numero > 0:
        temp = numero % 16
        if temp == 10: hexadecimal += 'A'
        elif temp == 11: hexadecimal += 'B'
        elif temp == 12: hexadecimal += 'C'
        elif temp == 13: hexadecimal += 'D'
        elif temp == 14: hexadecimal += 'E'
        elif temp == 15: hexadecimal += 'F'
        else: hexadecimal += str(temp)
        numero //= 16
    print('{} em base decimal = {} em base hexadecimal.'.format(decimal, hexadecimal[::-1]))
else:
    print('Base numérica não reconhecida!')
"""