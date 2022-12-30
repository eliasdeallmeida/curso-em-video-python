# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def fazerAreaTerreno(comprimento, largura):
    area = comprimento * largura
    print(f'A área do terreno vale {area} m^2')

print('-' * 50)
print(f'{"INFORME AS MEDIDAS DO TERRENO":^50}')
print('-' * 50)
comprimento = float(input('Comprimento [m]: '))
largura = float(input('Largura [m]: '))
fazerAreaTerreno(comprimento, largura)