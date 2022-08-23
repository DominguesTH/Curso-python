# DESAFIO: Crie um tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de futebol, na ordem de colocação. Depois mostre: A) Apenas os 5 primeiros colocados.  B) Os últimos 5 colocados da tabela. C) Uma lista com os times em ordem alfabpetica. D) Em que posição na tabela está o time da Chapecoense.

times = 'Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Internacional', 'Atlético-MG', 'América-MG', 'Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará SC', 'Fortaleza', 'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude'
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética:  {sorted(times)}')
print('-='*15)
print(f'O Santos está na {times.index("Santos") + 1}ª posição')
print('-='*15)
