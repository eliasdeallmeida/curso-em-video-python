# Aula 07 - Programa que recebe um valor em metros e converte para km, hm, dam, dm, cm e mm

print('========== DESAFIO 008 ==========')
print('Conversor de medidas')
m = float(input('Informe uma medida em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} metro(s) = {} quilômetro(s)'.format(m, km))
print('{} metro(s) = {} hectômetro(s)'.format(m, hm))
print('{} metro(s) = {} decâmetro(s)'.format(m, dam))
print('{} metro(s) = {} decímetro(s)'.format(m, dm))
print('{} metro(s) = {} centímetro(s)'.format(m, cm))
print('{} metro(s) = {} milímetro(s)'.format(m, mm))