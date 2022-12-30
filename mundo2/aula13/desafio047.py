# Aula 13 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('========== DESAFIO 047 ==========')
print('Os números pares no intervalo de 1 a 50 são:')
for cont in range(2, 50+1, 2):
    if cont < 50:
        print('{}, '.format(cont), end = '')
    else:
        print(cont)