import random

def sorteia():
    '''
    Retorna uma lista de numeros aleatorios
    '''
    lista = []

    for i in range(5):
        numero = random.randint(1,10)
        lista.append(numero)

    return lista

def soma_par(lista=[]):
    '''
    Soma itens de uma lista se ela for par.
    precisa ser exclusivamente de uma lista ou tupla
    '''
    soma = 0

    try:
        for i in lista:
            if i % 2 == 0:
                soma+=i
        return soma
    except TypeError:
        print('Insira uma lista somente de numeors inteiros')


numeros = sorteia()

soma_par = soma_par(numeros)

print(f'A soma dos numeros pares da lista {numeros} foi de {soma_par}')
