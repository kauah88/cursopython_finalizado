n= s = c = 0
while True:
    try:
        n = int(input('Digite um numero para somar (999 para sair): '))
    except ValueError:
        print('Digite somente numeros inteiros')
    if n == 999:
        break

    s+=n
    c+=1
print(f'A soma dos {c} valores foi de {s}')