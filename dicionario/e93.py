import time

estatistica = {}
lista_gols = []
total_gols = 0

estatistica['Nome_Jogador'] = input('Qual o nome do jogador: ')

while True:
    try:
        estatistica['Qtd_Partida'] = int(input(f'Quantas partidas {estatistica["Nome_Jogador"]} jogou? '))
        break

    except ValueError:
        print('Insira somente numeros')


for i in range(estatistica['Qtd_Partida']):
    gols = int(input(f'Quantos gols {estatistica["Nome_Jogador"]} fez na {i+1}° partida? '))
    lista_gols.append(gols)
    total_gols += gols

estatistica['Gols_partidas'] = lista_gols
estatistica['Total_Gols'] = total_gols

time.sleep(1)
print('-'*40)
print(f'O Jogador {estatistica["Nome_Jogador"]} jogou {estatistica["Qtd_Partida"]} partidas')
for i, v in enumerate(lista_gols):
    time.sleep(0.75)
    print(f'    -> Na {i+1}° partida ele fez {v} gols')

print(f'Fez um total de {estatistica['Total_Gols']} gols')