lista = []
lista_par = []
lista_impar = []
continuar = 's'
while continuar in ['s', 'sim']:

    while True:
        try:
            numero = int (input ('Insira um numero: '))
            lista.append(numero)
            break
        except ValueError:
            print('Inisra somente numeros inteiros')
            
    while True:
        try:
            continuar = input('Quer inserir mais algum numero? [s/n]')
            if continuar not in ['s','n']:
                print('Insira somente s para sim e n para nao')
            else: 
                break
        except ValueError:
            print('Insira somente s para sim e n para nao')
            
for n in lista:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'Esses forma todos os numeros inseridos: {lista}')
print(f'Esses foram os numeros impares: {lista_impar}')
print(f'Esses foram os numeros pares: {lista_par}')