import time

def maior(*nums):
    maior = 0
    print('Processando', end = ' ', flush = True)
    for i in range(3):
        time.sleep(0.8)
        print('.', end = ' ', flush = True)
    
    time.sleep(0.8) 
    print('\nValores passados: ', end = '')
    for i in nums:
        if i > maior:
            maior = i
        print(i, end =' ')

    print(f'\nForam passados {len(nums)} valores\nO maior foi o {maior}')

    

 
maior(1,2,3,3,2,1)