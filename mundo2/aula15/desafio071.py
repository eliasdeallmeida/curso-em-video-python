# Aula 15 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('========== DESAFIO 071 ==========')
print('{:=^45}'.format(' Bem vindo(a) ao Caixa Eletrônico '))
valor = int(input('Valor do saque: R$ '))
c50 = c20 = c10 = c1 = 0
while valor > 0:
    c50 = valor // 50
    valor -= c50 * 50
    c20 = valor // 20
    valor -= c20 * 20
    c10 = valor // 10
    valor -= c10 * 10
    c1 = valor
    valor -= c1
    if valor == 0:
        break
print('{:=^45}'.format(' Informações do saque '))
print(f'{c50} cédulas de R$ 50,00')
print(f'{c20} cédulas de R$ 20,00')
print(f'{c10} cédulas de R$ 10,00')
print(f'{c1} cédulas de R$ 1,00')