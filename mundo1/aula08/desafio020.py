# Aula 08 - Programa que recebe o nome de quatro alunos e sorteia a ordem de apresentação para um trabalho

from random import shuffle
print('========== DESAFIO 020 ==========')
print('Sorteador de nomes')
nome1 = str(input('1° nome: '))
nome2 = str(input('2° nome: '))
nome3 = str(input('3° nome: '))
nome4 = str(input('4° nome: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('Ordem de apresentação: {}'.format(lista))