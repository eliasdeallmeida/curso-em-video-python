# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')

def lerInteiro(mensagem):
    valor = 0
    while True:
        valor = str(input(mensagem))
        if valor.isnumeric():
            return int(valor)
        print('>>> ERRO: digite um valor inteiro.')

numero = lerInteiro('Digite um número: ')
print(f'Você digitou {numero}')