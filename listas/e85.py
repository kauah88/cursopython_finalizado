numeros = [[],[]]


for i in range (7):
    num = int(input(f'Digote o {i+1}° Valor: '))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print(numeros)
print(f'Os numeros pares foram: {numeros[0]}')
print(f'Os numeros impares foram: {numeros[1]}')