# Aula 08 - Programa que recebe um ângulo e mostra seu seno, cosseno e tangente

from math import sin, cos, tan, radians
print('========== DESAFIO 018 ==========')
print('Calculadora de seno, cosseno e tangente')
x = int(input('Informe um ângulo: '))
seno = sin(radians(x))
cosseno = cos(radians(x))
tangente = tan(radians(x))
print('sen({}°) = {:.2f}'.format(x, seno))
print('cos({}°) = {:.2f}'.format(x, cosseno))
print('tan({}°) = {:.2f}'.format(x, tangente))