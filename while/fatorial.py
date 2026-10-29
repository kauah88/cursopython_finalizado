numero = int(input('Qual numero deseja saber o fatorial? '))
aux = numero
fatorial = 1


print(f'{numero}! =', end=' ')
while aux > 0:
    print(f'{aux}', end=' ')
    print('x' if aux > 1 else '=', end=' ')
    fatorial *= aux
    aux-=1
print(fatorial)

