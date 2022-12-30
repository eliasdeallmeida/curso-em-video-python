# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def avaliarSituacaoParaVotacao(anoNascimento):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return f'Com {idade} anos de idade: voto NEGADO'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos de idade: voto OPCIONAL'
    return f'Com {idade} anos de idade: voto OBRIGATÓRIO'

print(f'{"VALIDAÇÃO PARA PARTICIPAÇÃO DAS ELEIÇÕES":^50}')
anoNascimento = int(input('Ano de nascimento: '))
print(avaliarSituacaoParaVotacao(anoNascimento))