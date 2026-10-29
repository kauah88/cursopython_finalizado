matriz = [[], [], []]

for i in range(3): 
    for j in range(3):
        num = int(input(f'Insira o valor para {[i], [j]}: '))
        matriz[i].append(num)

for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]} ]', end = ' ')
    print()