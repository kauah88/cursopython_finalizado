valor = int(input('Quanto vc quer sacar? '))
cont_50 = cont_20 = cont_10 = cont_1 = 0
total = valor

while total > 0:
    if total >= 50:
        total-=50
        cont_50+=1

    elif total >= 20:
        total-=20
        cont_20+=1

    elif total >= 10:
        total-=10
        cont_10+=1

    else:
        total-=1
        cont_1+=1

print (f'Voce sacou {valor}! ')
if cont_50 > 0:
    print(f'total de {cont_50} cedulas de R$50')

if cont_20 > 0:
    print(f'total de {cont_20} cedulas de R$20')

if cont_10 > 0:
    print(f'total de {cont_10} cedulas de R$10')

if cont_1 > 0:
    print(f'total de {cont_1} cedulas de R$1')
