def lerValorInteiro(mensagem):
    valido = False
    while not valido:
        try:
            entrada = int(input(mensagem))
        except(ValueError, TypeError):
            print(f'>>> ERRO: Digite um número inteiro válido!')
        except(KeyboardInterrupt):
            print('>>> ERRO: o usuário preferiu não informar um número inteiro!')
            return '<vazio>'
        else:
            valido = True
    return entrada

def lerTexto(mensagem):
    valido = False
    while not valido:
        try:
            entrada = str(input(mensagem))
        except(ValueError, TypeError):
            print(f'>>> ERRO: Digite um texto válido!')
        except(KeyboardInterrupt):
            print('>>> ERRO: o usuário preferiu não informar um texto!')
            return '<vazio>'
        else:
            valido = True
    return entrada