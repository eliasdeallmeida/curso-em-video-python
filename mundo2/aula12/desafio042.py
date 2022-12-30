# Aula 12 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado (Equilátero, Isósceles ou Escaleno).

print('========== DESAFIO 042 ==========')
print('Informe a medida dos três lados de um triãngulo que eu direi que tipo de triãngulo é possível formar.')
r1 = float(input('1ª reta: '))
r2 = float(input('2ª reta: '))
r3 = float(input('3ª reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com as retas {}, {} e {} possível formar um triângulo '.format(r1, r2, r3), end = '')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Não é possível formar um triângulo com as medidas informadas!')