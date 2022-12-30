# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

print('========== DESAFIO 080 ==========')
lista = []
for c in range(0, 5):
    num = int(input(f'Digite o {c+1}º número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        for i in range(len(lista)):
            if num <= lista[i]:
                lista.insert(i, num)
                break
print(f'Valores digitados: {lista}')