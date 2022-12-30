# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

def mostrarTitulo(titulo):
    espacoUnilateral = 5
    tamanhoTotal = len(titulo) + espacoUnilateral * 2
    print('~' * tamanhoTotal)
    print(f'{" " * espacoUnilateral}{titulo}')
    print('~' * tamanhoTotal)

def mostrarInstrucoes(comando):
    mostrarTitulo(f'Acessando o manual do comando "{comando}"')
    help(comando)

comando = ''
while True:
    mostrarTitulo('SISTEMA DE AJUDA')
    comando = str(input('Função ou biblioteca: ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        mostrarInstrucoes(comando)
mostrarTitulo('ATÉ A PRÓXIMA!')