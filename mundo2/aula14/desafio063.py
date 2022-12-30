# Aula 14 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('========== DESAFIO 063 ==========')
print('Gerador de Sequência de Fibonacci')
total = int(input('Informe a quantidade de termos que deseja mostrar: '))
cont = 1
primeiro = 0
segundo = 1
while cont <= total:
    if cont == 1:
        atual = primeiro
        print('{} ->'.format(atual), end = ' ')
    elif cont == 2:
        atual = segundo
        anterior = primeiro
        print('{} ->'.format(atual), end = ' ')
    else:
        temp = anterior
        anterior = atual
        atual += temp
        print('{} ->'.format(atual), end = ' ')
    cont += 1
print('FIM')