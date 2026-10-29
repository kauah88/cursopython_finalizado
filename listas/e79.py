lista = []
continuar = 's'

while continuar == 's':
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
        print('Numero adicionado.')
    else:
        print('Numero ja esta na lista')
        

    while True:
        continuar = input('\nQuer continuar? [s/n] ')
        if continuar in ['sim', 's', 'nao', 'n']:
            break
        else:
            print('Insira somente [s] para sim ou [n] para não')

tamanho_lista = len(lista) #para quando for imprimir criar um separador de "-", e quando for o ultimo numero da lista ele imprime um end = ' ' para nao ficar um - no final
lista.sort()

print('Os numeros inseridos foram: ')
for i, n in enumerate(lista):
    if i == tamanho_lista - 1:
        print(n, end = ' ')

    else:
        print(n, end = ' - ')