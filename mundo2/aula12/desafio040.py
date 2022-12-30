# Aula 12 - Crie um programa que leia duas notas dde um aluno e calcula sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0 (REPROVADO); Média entre 5.0 e 6.9 (RECUPERAÇÃO); Média 7.0 ou superior (APROVADO).

print('========== DESAFIO 040 ==========')
nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('Média {:.1f}: APROVADO!'.format(media))
elif 5.0 <= media < 7.0:
    print('Média {:.1f}: RECUPERAÇÃO!'.format(media))
else:
    print('Média {:.1f}: REPROVADO!'.format(media))