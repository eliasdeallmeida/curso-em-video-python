# Aula 08 - Programa que recebe o nome de quatro alunos e sorteia um deles para apagar o quadro

from random import choice
print('========== DESAFIO 019 ==========')
print('Sorteador de nomes')
nome1 = str(input('1° nome: '))
nome2 = str(input('2° nome: '))
nome3 = str(input('3° nome: '))
nome4 = str(input('4° nome: '))
lista = [nome1, nome2, nome3, nome4]
escolha = choice(lista)
print('A pessoa escolhida foi {}!'.format(escolha))