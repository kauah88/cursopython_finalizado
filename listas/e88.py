import random

n_jogos = int(input('Quantos jogos voce quer sortear? '))
lista_jogos = []

for i in range(n_jogos):
    sublista_jogos = []
    
    while len (sublista_jogos) < 6:
        numeros_rand = random.randint(1,60)

        if numeros_rand not in sublista_jogos:
            sublista_jogos.append(numeros_rand)
    sublista_jogos.sort()
    lista_jogos.append(sublista_jogos)

for i, v in enumerate(lista_jogos):
    print(f'{i+1}° jogo: {v}')
print(lista_jogos)