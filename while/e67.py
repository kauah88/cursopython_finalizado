n = m = 0
while True:
    c = 1
    n = int(input('Qual numero deseja saber a tabuada? '))
    if n < 0 :
        break

    while c <= 10:
        m = n * c
        print(f'{n} x {c} = {m}')
        c+=1
