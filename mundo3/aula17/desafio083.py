# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

print('========== DESAFIO 083 ==========')
expressao = []
aberturas = fechamentos = 0
entrada = str(input(('Digite uma expressão matemática: ')))
for c in entrada:
    expressao.append(c)
for c in expressao:
    if aberturas < fechamentos:
        break
    elif '(' in c:
        aberturas += 1
    elif ')' in c:
        fechamentos += 1
if aberturas == fechamentos:
    print('Expressão válida!')
else:
    print('Expressão inválida!')