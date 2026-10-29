n1 = 0
n2 = 0
n3 = 0
n4 = 0


while True:
    try:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))
        n3 = int(input('Digite um valor: '))
        n4 = int(input('Digite um valor: '))
        break
    except ValueError:
        print('Insira somente numeros inteiros!')

numeros = (n1, n2, n3, n4)
print(numeros)

#contador de 9
cont_9 = 0
for n in numeros:
    if n == 9:
        cont_9+=1

if cont_9 > 0:
    print(f'O numero 9 apareceu {cont_9} vezes')
else:
    print('O numero 9 nao esta na tupla')

#posição do 3
cont_3 = 0
 
if 3 in numeros:
            print(f'O primeiro numero 3 apareceu na {numeros.index(3)+1}ª posição da tupla ')
else:
    print('O numero 3 nao esta na tupla')
        
    

#numeros pares
cont_par = 0 

for n in numeros: #para saber se tem numeros pares na tupla
    if n % 2 == 0:
        cont_par+=1

if cont_par > 0: 
    print(f'Os numeros pares foram', end=' ')
    for n in numeros: # para printrar os numeros pares
        if n % 2 == 0:
            print(n, end = ' ')
            cont_par+=1
else: 
    print('nao existem numeros pares na tupla')


