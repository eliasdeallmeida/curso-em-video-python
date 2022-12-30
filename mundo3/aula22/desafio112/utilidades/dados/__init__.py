def lerValor(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: "{entrada}" não é um valor válido!')
            continue
        valido = True
    return float(entrada)