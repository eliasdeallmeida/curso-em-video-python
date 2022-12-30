# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

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

def lerValorReal(mensagem):
    valido = False
    while not valido:
        try:
            entrada = float(input(mensagem))
        except(ValueError, TypeError):
            print(f'>>> ERRO: Digite um número real válido!')
        except(KeyboardInterrupt):
            print('>>> ERRO: o usuário preferiu não informar um número real!')
            return '<vazio>'
        else:
            valido = True
    return entrada

valorInteiro = lerValorInteiro('Digite um número inteiro: ')
valorReal = lerValorReal('Digite um número real: ')
print(f'O valor inteiro foi {valorInteiro} e o valor real foi {valorReal}')