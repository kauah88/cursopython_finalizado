lista = []

maior = menor = 0

for i in range(5):
    while True:
        try:
            #lista.append(int(input(f'Digite o valor da {i}° posição: ')))
            lista = [ 5, 5, 3, 1, 1]
            break
        except ValueError:
            print('insira somente numeros inteiros')

    if i == 0:
        menor = maior = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]

        if lista[i] < menor:
            menor = lista[i]
print('Voce digitou os valores: ', end='')
for v in lista:
    print(v, end=' ')
    
print()
print(f'O maior valor foi o {maior} nas posições', end =' ')
for i, v in enumerate(lista):
    if v == maior:
        print(i, end = ' ')

