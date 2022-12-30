'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

dados = dict()
pessoas = list()
qtd_pessoas = soma_idade = 0

while True:
    print('-=' * 30)
    dados['Nome'] = str(input('Nome: ')).title()

    while True:
        dados['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('>>> ERRO: Digite M ou F para o sexo.')

    while True:
        dados['Idade'] = int(input('Idade: '))
        if dados['Idade'] >= 0:
            break
        print('>>> ERRO: Digite uma idade maior ou igual de zero.')
    
    soma_idade += dados['Idade']
    qtd_pessoas += 1
    pessoas.append(dados.copy())
    dados.clear()

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('>>> ERRO: Digite S para SIM ou N para NÃO.')
    
    if continuar == 'N':
        media_idade = soma_idade / qtd_pessoas
        break

print('-=' * 30)
print(f'Foram cadastradas {qtd_pessoas} pessoas')
print(f'A média de idade das pessoas é {media_idade}')

print('Os nomes das mulheres informadas foram ', end = '')
for p in pessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end = '')
print()

print('As pessoas com idade acima da média foram ', end = '')
for p in pessoas:
    if p['Idade'] > media_idade:
        print(f'{p["Nome"]} ', end = '')
print()

print('-=' * 30)