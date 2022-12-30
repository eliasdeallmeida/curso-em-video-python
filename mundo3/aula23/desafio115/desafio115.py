# Vamos criar um menu em Python, usando modularização.

from library.interface import *
from library.input import *
from library.arquivo import *

arquivo = 'cadastros.txt'
arquivoExiste = verificarSeArquivoExiste(arquivo)

if not arquivoExiste:
    criarArquivo(arquivo)

while True:
    opcao = menu(['Ver usuários cadastrados', 'Cadastrar usuário', 'Sair'])
    if opcao == 1:
        lerArquivo(arquivo)
    elif opcao == 2:
        mostrarTextoFormatado('NOVO CADASTRO')
        nome = lerTexto('Nome: ')
        idade = lerValorInteiro('Idade: ')
        cadastrarUsuario(arquivo, nome, idade)
    elif opcao == 3:
        mostrarTextoFormatado('Saindo do sistema...')
        break