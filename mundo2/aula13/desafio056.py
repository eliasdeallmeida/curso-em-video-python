# Aula 13 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print('========== DESAFIO 056 ==========')
print('Informe o nome, a idade e o sexo de 4 pessoas')

mediaIdade = float(0)
iMaisVelho = int(0)
nMaisVelho = ''
menosq20 = int(0)

for cont in range(1, 4 + 1):
    print('----- Dados da {}ª pessoa -----'.format(cont))
    nome = str(input('1) Nome: ')).strip()
    idade = int(input('2) Idade: '))
    sexo = str(input('3) Sexo (M/F): ')).strip().upper()

    mediaIdade += idade

    if sexo == 'M' and nMaisVelho == '' and iMaisVelho == 0:
        nMaisVelho = nome
        iMaisVelho = idade
    elif sexo == 'M' and idade > iMaisVelho:
        nMaisVelho = nome
        iMaisVelho = idade
    
    if sexo == 'F' and idade < 20:
        menosq20 += 1

mediaIdade /= 4
print('A média de idade é igual a {:.1f} anos.'.format(mediaIdade))
print('O nome do homem mais velho é {}.'.format(nMaisVelho))
print('Dentre as mulheres, {} delas tem menos que 20 anos.'.format(menosq20))