# Aula 13 - Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('========== DESAFIO 049 ==========')
print('Calculadora de tabuada (1 a 10)')
num = int(input('Digite um número: '))
print('-' * 12)
for tbd in range(1, 10+1):
    print('{} x {:2} = {}'.format(num, tbd, num * tbd))
print('-' * 12)