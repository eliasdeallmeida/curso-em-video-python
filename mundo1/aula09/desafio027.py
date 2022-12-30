# Aula 09 - Programa que recebe o nome completo de uma pessoa e exibe o primeiro e o último nome separadamente

print('========== DESAFIO 027 ==========')
nome = str(input('Digite seu nome completo: ')).strip()
nomeDividido = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}'.format(nomeDividido[0], nomeDividido[len(nomeDividido) - 1]))