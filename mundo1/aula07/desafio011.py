# Aula 07 - Programa que recebe a altura e largura de uma parede em metros, calcula a área a mostra a quantidade de tinta necessária para pintá-la (sabendo que 1 litro de tinta pinta uma área de 2 metros quadrados)

print('========== DESAFIO 011 ==========')
altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))
area = altura * largura
qtdTinta = area / 2
print('A parede tem dimensão de {} x {} e mede {:.2f} metros quadrados'.format(altura, largura, area))
print('Para pintar a parede são necessários {:.1f} litros de tinta'.format(qtdTinta))