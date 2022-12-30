# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = {}
anos_contribuição = 35
ano_atual = date.today().year

print('-=' *25)
print(f'{"PREENCHA OS DADOS ABAIXO":^50}')
print('-=' * 25)

dados['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = ano_atual - ano_nascimento
dados['CTPS'] = int(input('CTPS [Zero caso não tenha]: '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Contratação: '))
    dados['Salário'] = float(input('Salário: '))
    anos_contribuição -= ano_atual - dados['Contratação']
    if anos_contribuição > 0:
        dados['Aposentadoria'] = 'Restando ' + str(anos_contribuição) + ' anos de contribuição'
    else:
        dados['Aposentadoria'] = 'Aposentadoria disponível'


print('-=' * 25)
print(f'{"SEUS DADOS":^50}')
print('-=' * 25)

for indice, conteudo in dados.items():
    print(f'{indice:<15}{conteudo:>35}')

print('-=' * 25)