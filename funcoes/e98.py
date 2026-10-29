import time

def contador(inicio, fim, passo):
    cont = inicio

    if passo == 0:
        passo = 1

    elif passo < 0:
        passo = abs(passo)

    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end = " ", flush = True)

            cont+=passo
            time.sleep(0.5)

    else:
        cont = inicio
        while cont >= fim:
            print(cont)

            cont -= passo
            time.sleep(1)
    print('FIM!')


#Principal

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)