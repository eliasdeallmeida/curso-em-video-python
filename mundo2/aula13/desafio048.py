# Aula 13 - Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('========== DESAFIO 048 ==========')
soma = int(0)
for cont in range(1, 500+1):
    if cont % 3 == 0:
        soma += cont
print('A soma dos múltiplos de 3 no intervalo de 1 à 500 vale {}.'.format(soma))