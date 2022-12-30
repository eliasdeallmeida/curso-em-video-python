# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times; b) Os últimos 4 colocados; c) Times em ordem alfabética; d) Em que posição está o time da Chapecoense.

print('========== DESAFIO 073 ==========')
times = ('Palmeiras', 'Flamengo', 'Corinthians', 'Internacional', 'Fluminense', 'Atlético-PR', 'Atlético-MG', 'América-MG', 'Santos', 'Bragantino', 'Goiás', 'Fortaleza', 'Botafogo', 'São Paulo', 'Ceará', 'Cuiabá', 'Coritiba', 'Avaí', 'Atlético-GO', 'Juventude')
print(f'Os primeiros 5 times são {times[0:5]}')
print(f'Os 4 últimos colocados são {times[-4:]}')
print(f'Os times em ordem alfabética são {sorted(times)}')
print(f'O Ceará está na posição {times.index("Ceará")+1}')