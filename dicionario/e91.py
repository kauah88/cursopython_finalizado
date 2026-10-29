import random
import time 
from operator import itemgetter

jogadores = {
    'jogador 1' : random.randint(1,6),
    'jogador 2' : random.randint(1,6),
    'jogador 3' : random.randint(1,6),
    'jogador 4' : random.randint(1,6)
    }
ranking = list()

print('Valores sorteados')
for c, v in jogadores.items():
    print(f'    O {c} tirou {v}')
    time.sleep(0.75)

ranking = sorted(jogadores.items(), key = itemgetter(1), reverse=True)

print('ranking dos jogadores')

for i, v in enumerate(ranking):
    print(f'    {i+1}° posição {v[0]} com {v[1]}')
    time.sleep(0.75)

