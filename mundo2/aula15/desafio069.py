# Aula 15 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: (A) quantas pessoas tem mais de 18 anos; (B) quantos homens foram cadastrados; (C) quantas mulheres tem menos de 20 anos.

print('========== DESAFIO 069 ==========')
maiorDeIdade = hTotal = mMenor20 = 0
while True:
    print('{: ^35}'.format(' Cadastre-se aqui '))
    print('-' * 25)
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    print('-' * 25)
    if idade >= 18: maiorDeIdade += 1
    if sexo == 'M': hTotal += 1
    if sexo == 'F' and idade < 20: mMenor20 += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('\n')
    if continuar != 'S': break
print(f'{maiorDeIdade} pessoas tem mais de 18 anos.')
print(f'{hTotal} homens cadastrados.')
print(f'{mMenor20} mulheres com menos de 20 anos cadastradas.')