# Aula 08 - Programa que recebe o tamanho do cateto oposto e do cateto adjacente de um triângulo retângulo e mostra o valor da hipotenusa

from math import hypot
print('========== DESAFIO 017 ==========')
co = float(input('Informe o tamanho do cateto oposto: '))
ca = float(input('Informe o tamanho do cateto adjacente: '))
h = hypot(co, ca)
print('Um triângulo retângulo cateto oposto = {} e cateto adjacente = {} tem a hipotenusa = {:.1f}'.format(co, ca, h))