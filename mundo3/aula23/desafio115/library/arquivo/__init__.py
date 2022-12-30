from library.interface import *

def verificarSeArquivoExiste(nomeDoArquivo):
    try:
        arquivo = open(nomeDoArquivo, 'rt')
        arquivo.close()
    except(FileNotFoundError):
        return False
    else:
        return True

def criarArquivo(nomeDoArquivo):
    try:
        arquivo = open(nomeDoArquivo, 'wt+')
        arquivo.close()
    except:
        print('>>> ERRO: Não foi possível criar o arquivo!')
    else:
        print('>>> SUCESSO: O arquivo foi criado corretamente!')

def lerArquivo(nomeDoArquivo):
    try:
        arquivo = open(nomeDoArquivo, 'rt')
    except:
        print('>>> ERRO: Ocorreu um problema na leitura do arquivo!')
    else:
        mostrarTextoFormatado('USUÁRIOS CADASTRADOS')
        imprimirLinha()
        for linha in arquivo:
            dado = linha.split(';')
            ultimaPosicao = len(dado) - 1
            dado[ultimaPosicao] = dado[ultimaPosicao].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')
    finally:
        arquivo.close()

def cadastrarUsuario(nomeDoArquivo, nome = 'desconhecido', idade = 0):
    try:
        arquivo = open(nomeDoArquivo, 'at')
    except:
        print('>>> ERRO: Não foi possível abrir o arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('>>> ERRO: Não foi possível cadastrar usuário!')
        else:
            print('>>> SUCESSO: Usuário cadastrado com sucesso!')
            arquivo.close()