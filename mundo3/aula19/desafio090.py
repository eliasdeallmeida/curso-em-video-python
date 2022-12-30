# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

boletim = {}

print('-=' * 15)
boletim['Nome'] = str(input('Nome do aluno: '))
boletim['Média'] = float(input('Média final: '))

if boletim['Média'] < 5:
    boletim['Situação'] = 'Reprovado'
elif boletim['Média'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Aprovado'

print('-=' * 15)
for indice, conteudo in boletim.items():
    print(f'{indice}: {conteudo}')
print('-=' * 15)