'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''

def fazerEstatisticas(*notasAlunos, situacao = False):
    dados = dict()
    dados['Maior nota'] = max(notasAlunos)
    dados['Menor nota'] = min(notasAlunos)
    dados['Média da turma'] = f'{sum(notasAlunos) / len(notasAlunos):.2f}'
    if situacao is True:
        if float(dados['Média da turma']) < 5:
            dados['Situação'] = 'RUIM'
        elif float(dados['Média da turma']) < 7:
            dados['Situação'] = 'RAZOÁVEL'
        else:
            dados['Situação'] = 'BOA'
    return dados

estatisticas = fazerEstatisticas(5.5, 10, 7.5, 8.8, situacao = True)
print(estatisticas)