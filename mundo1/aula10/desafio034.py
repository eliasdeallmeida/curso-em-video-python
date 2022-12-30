# Aula 10 - Programa que recebe um valor de salário e calcula seu aumento. Se salário é maior que R$ 1250,00 o aumento será de 10%, se não, o aumento será de 15%

print('========== DESAFIO 034 ==========')
salario = float(input('Informe seu salário: R$ '))
if salario > 1250.00:
    novoSalario = salario + (10/100 * salario)
    print('Seu salário após o aumento de 10% será de R$ {:.2f}.'.format(novoSalario))
else:
    novoSalario = salario + (15/100 * salario)
    print('Seu salário após o aumento de 15% será de R$ {:.2f}.'.format(novoSalario))