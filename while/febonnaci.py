n_termos = int(input('Quantos termos da sequencia de Fibonnaci deseja ver? '))
cont = 2
n1 = 0
n2 = 1

if n_termos == 1:
    print(n1)
    
elif n_termos == 2:
    print(f'{n1} ➝  {n2}')
    
else:
    print(f'{n1} ➝  {n2}', end =' ')
    
while cont < n_termos  and n_termos > 2:
    feb = n1 + n2
    print(f' ➝  {feb}', end=' ')
    n1 = n2
    n2 = feb
    cont+=1
print("FIM")