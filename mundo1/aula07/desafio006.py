# Aula 07 - Programa que recebe um número e mostra o dobro, o triplo e a raiz quadrada

print('========== DESAFIO 006 ==========')
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz2 = num ** (1/2)
print('Dobro =', dobro)
print('Triplo =', triplo)
print('Raiz quadrada = {:.3f}'.format(raiz2))