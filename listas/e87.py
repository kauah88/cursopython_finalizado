matriz = [[], [], []]

soma_par = soma_3col = maior_valor2lin = 0

for i in range(3): 
    for j in range(3):
        num = int(input(f'Insira o valor para {[i], [j]}: '))
        matriz[i].append(num)

        #para saber a soma de todos os valores
        if num % 2 == 0:
            soma_par += num

        #soma da 3 coluna
        if j == 2:
            soma_3col +=num

        #maior valor da segunda linha 
        if i == 1:
            if(matriz[i][j]) > maior_valor2lin:
                maior_valor2lin = matriz[i][j]
        

for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]} ]', end = ' ')

    print()

print(f'A soma de todos os valores pares e de: {soma_par}')
print(f'A soma dos valores da terceira coluna e de : {soma_3col}')
print(f'O maior valor da segunda linha e o {maior_valor2lin}')