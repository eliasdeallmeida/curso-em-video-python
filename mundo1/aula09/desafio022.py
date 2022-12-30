# Aula 09 - Programa que recebe o nome completo do usuário e mostra o nome com todas as letras maiúsculas, todas as letras minúsculas, quantidade de caracteres sem considerar espaços e quantas letras tem o primeiro nome

print('========== DESAFIO 022 ==========')
nome = str(input('Informe seu nome completo: '))
print('Seu nome apenas com letras maiúsculas:', nome.upper())
print('Seu nome apenas com letras minúsculas:', nome.lower())
print('Quantidades total de letras:', len(nome) - nome.count(' '))
print('Quantidade de letras no primeiro nome:', nome.find(' '))