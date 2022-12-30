# Aula 10 - Programa que recebe o tamanho de 3 retas e informa se é possível ou não formar um triângulo

print('========== DESAFIO 035 ==========')
print('Informe o valor de 3 retas e eu direi se é ou não possível formar um triângulo com elas.')
reta1 = float(input('Digite o tamanho da 1ª reta: '))
reta2 = float(input('Digite o tamanho da 2ª reta: '))
reta3 = float(input('Digite o tamanho da 3ª reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')