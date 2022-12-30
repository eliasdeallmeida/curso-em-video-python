# Aula 07 - Programa que converte uma temperatura em graus Celsius e converte para graus Fahrenheit

print('========== DESAFIO 014 ==========')
print('Conversor de Celsius para Fahrenheit')
tc = float(input('Informe a temperatura em °C: '))
tf = tc * 9/5 + 32
print('{:.1f}°C = {:.1f}°F'.format(tc, tf))