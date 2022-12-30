# Aula 06 - Programa que recebe algo do teclado e informa as informações do que foi digitado

print('========== DESAFIO 004 ==========')
x = input('Digite algo: ')
print('O tipo primitivo é', type(x))
print('Só tem espaços?', x.isspace())
print('É número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em minúsculas?', x.islower())
print('Está em maiúsculas?', x.isupper())
print('Está capitalizado?', x.istitle())