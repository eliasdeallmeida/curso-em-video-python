# Aula 07 - Programa que recebe duas notas de um aluno, calcula e mostra a média

print('========== DESAFIO 007 ==========')
print('Calculadora de média entre duas notas')
nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
media = (nota1 + nota2) / 2
print('A média entre {} e {} vale {:.1f}'.format(nota1, nota2, media))