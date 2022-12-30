# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('========== DESAFIO 076 ==========')
produtos = ('Biscoito', 2.25, 'Leite', 5, 'Margarina', 3.5)
print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 40)
for c in range(len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end = '')
    else:
        print(f'R$ {produtos[c]:>7.2f}')
print('-' * 40)