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
    return f'{moeda} {valor:.2f}'.replace('.', ',')

def mostrarResumo(valor = 0, taxa = 0, formatar = False):
    print(f'{" RESUMO DOS CÁLCULOS ":=^50}')
    print(f'{"Valor informado":.<30}{formatarValorMonetario(valor):.>20}')
    print(f'{f"Valor com aumento de {taxa}%":.<30}{calcularAumentoDoValor(valor, taxa, formatar):.>20}')
    print(f'{f"Valor com redução de {taxa}%":.<30}{calcularReducaoDoValor(valor, taxa, formatar):.>20}')
    print(f'{"Dobro do valor":.<30}{calcularDobroDoValor(valor, formatar):.>20}')
    print(f'{"Metade do valor":.<30}{calcularMetadeDoValor(valor, formatar):.>20}')