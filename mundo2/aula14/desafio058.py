# Aula 14 - Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('========== DESAFIO 058 ==========')
print('Jogo de Adivinhação em Python 2.0')
print('Pensei em um número de 0 a 10, você é capaz de adivinhar qual é?')
numeroSecreto = randint(0, 10)
tentativas = 0
acertou = False
while not acertou:
    chute = int(input('Qual seu chute? '))
    tentativas += 1
    if chute == numeroSecreto:
        acertou = True
    elif chute > numeroSecreto:
        print('Tente um número menor. Vamos de novo!')
    elif chute < numeroSecreto:
        print('Tente um número maior. Vamos de novo!')
print('Parabéns!!! O número secreto era {}!'.format(numeroSecreto))
print('Você precisou de {} tentativa(s) para acertar.'.format(tentativas))