# Aula 09 - Programa que recebe uma frase do teclado e mostra quantas letras "A" existem, em que posição ela aparece pela primeira vez e em que posição ela aparece pela última vez

print('========== DESAFIO 026 ==========')
print('Contador de letra "A"')
frase = input('Digite uma frase: ').strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))