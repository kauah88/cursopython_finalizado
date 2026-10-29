lista = []


for i in range(5):
    numero = int(input('Digite um numero: '))

    if i == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        i = 0

        while i < len(lista):
            if numero <= lista[i]:
                lista.insert(i, numero)
                break
            i += 1

print(lista)