# Aula 14 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('========== DESAFIO 057 ==========')
sexo = str('')
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Seu sexo é {}.'.format(sexo))