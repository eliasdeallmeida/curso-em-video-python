# Aula 13 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print('========== DESAFIO 053 ==========')
print('Verificador de palíndromos')
frase = str(input('Digite uma frase: ')).strip().upper().split()
frase = ''.join(frase)
palindromo = ''
for i in range(len(frase) - 1, -1, -1):
    palindromo += str(frase[i])
print('A frase {} depois de ser invertida equivale a {}.'.format(frase, palindromo))
if frase == palindromo:
    print('Portanto, É PALÍNDROMO!')
else:
    print('Portanto, NÃO É PALÍNDROMO!')