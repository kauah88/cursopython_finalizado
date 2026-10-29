import time 

def fatorial (num, show = False):
    '''
    Retorna o falor do fatorial, mas se show for True mostra o calculo e printa o fatorial

    '''
    fatorial = 1

    for i in range (num, 0, -1):
        fatorial *= i

    if not show:
        return fatorial

    else:
        for i in range(num, 0, -1):

            if i > 1:
                print(i , end = ' ', flush=True)
                time.sleep(0.3)
                print('x', end = ' ', flush=True)
                time.sleep(0.3)

            else:
                print(i , end = ' ', flush=True)
                time.sleep(0.3)
                print('=' , end = ' ', flush=True)
                time.sleep(0.3)

        return fatorial

print(fatorial(5, True))