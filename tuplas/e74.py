import random

n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
n4 = random.randint(0,9)
n5 = random.randint(0,9)

maior_numero = menor_numero = 0
numeros_random = (n1,n2,n3,n4,n5)

print('Os numeros sorteados foram: ', end="")
for i in range(len(numeros_random)):
    print(numeros_random[i], end=' ')

    if i == 0:
        menor_numero = numeros_random[i]
    if numeros_random[i] > maior_numero:
        maior_numero = numeros_random[i]
    if numeros_random[i] < menor_numero:
        menor_numero = numeros_random[i]

print(f'\nO maior numero foi: {maior_numero}')
print(f'O menor numero foi: {menor_numero}')



    