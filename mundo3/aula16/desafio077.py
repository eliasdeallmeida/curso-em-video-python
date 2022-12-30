#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print('========== DESAFIO 077 ==========')
palavras = ('Computador', 'Amor', 'Tecnologia', 'Futuro', 'Escola')
for p in palavras:
    print(f'\nA palavra {p.upper()} tem as vogais ', end = '')
    for l in p:
        if l.lower() in 'aeiou':
            print(f'{l.upper()}', end = ' ')