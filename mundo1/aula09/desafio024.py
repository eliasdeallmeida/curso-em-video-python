# Aula 09 - Programa que recebe um nome de cidade e verifica se o nome começa com "Santo"

print('========== DESAFIO 024 ==========')
print('Verificador de strings')
cidade = input('Digite um nome de cidade: ')
cidade = cidade.strip()
print('O nome dessa cidade começa com "Santo"?', cidade[:5].title() == 'Santo')