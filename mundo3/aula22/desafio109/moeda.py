def calcularAumentoDoValor(valor = 0, taxaDeAumento = 0, formatar = False):
    valor += valor * taxaDeAumento / 100
    return valor if formatar is False else formatarValorMonetario(valor)

def calcularReducaoDoValor(valor = 0, taxaDeReducao = 0, formatar = False):
    valor -= valor * taxaDeReducao / 100
    return valor if formatar is False else formatarValorMonetario(valor)

def calcularDobroDoValor(valor = 0, formatar = False):
    valor *= 2
    return valor if formatar is False else formatarValorMonetario(valor)

def calcularMetadeDoValor(valor = 0, formatar = False):
    valor /= 2
    return valor if formatar is False else formatarValorMonetario(valor)

def formatarValorMonetario(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')