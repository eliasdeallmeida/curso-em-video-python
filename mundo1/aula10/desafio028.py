# Aula 10 - Programa que sorteia um número entre 0 e 5 e pede para o usuário tentar acertar

from random import randint
print('========== DESAFIO 028 ==========')
num = randint(0, 5)
print('Pensei em um número entre 0 e 5. Tente adivinhar!')
chute = int(input('Seu palpite: '))
if chute == num:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Eu pensei no número {}.'.format(num))