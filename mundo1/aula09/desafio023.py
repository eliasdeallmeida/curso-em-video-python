# Aula 09 - Programa que recebe um número de 0 a 9999 e mostra na tela cada um dos dígitos separadamente

print('========== DESAFIO 023 ==========')
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
print('Avaliando o número informado, ele tem:')
print('Unidade =', u)
print('Dezena =', d)
print('Centena =', c)
print('Unidade de milhar =', um)