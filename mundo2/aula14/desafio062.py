# Aula 14 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('========== DESAFIO 062 ==========')
print('Gerador de Progressão Aritmética')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = 1
limite = 10
termoAtual = primeiro
while termo <= limite:
    print('{} ->'.format(termoAtual), end = ' ')
    termoAtual += razao
    termo += 1
    if termo > limite:
        print('?', end = '')
        aumentaPA = int(input('\nQuantos termos deseja mostrar a mais na PA? '))
        limite += aumentaPA
print('FIM')