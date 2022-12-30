def calcularAumentoDoValor(valor = 0, taxaDeAumento = 0):
    return valor + valor * taxaDeAumento / 100

def calcularReducaoDoValor(valor = 0, taxaDeReducao = 0):
    return valor - valor * taxaDeReducao / 100

def calcularDobroDoValor(valor = 0):
    return valor * 2

def calcularMetadeDoValor(valor = 0):
    return valor / 2

def formatarValorMonetario(valor = 0, moeda = 'R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')