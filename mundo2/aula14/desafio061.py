# Aula 14 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('========== DESAFIO 061 ==========')
print('Gerador de Progressão Aritmética')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
termoAtual = primeiro
while cont <= 10:
    print('{} -> '.format(termoAtual), end = '')
    termoAtual += razao
    cont += 1
print('FIM')