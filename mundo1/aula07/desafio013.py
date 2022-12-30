# Aula 07 - Programa que recebe um salário e mostre seu novo valor com um aumento de 15%

print('========== DESAFIO 013 ==========')
print('Ajuste salarial')
salario = float(input('Informe seu salário: '))
novoSalario = salario + (15/100 * salario)
print('O salário de R$ {:.2f} após o aumento de 15% vale R$ {:.2f}'.format(salario, novoSalario))