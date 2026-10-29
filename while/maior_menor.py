continuar = 's'
soma = num = maior_num = menor_num = cont = 0

while continuar == 's':
    num = int( input('Digite um numero '))
    cont += 1
    soma += num

    if cont == 1:
        menor_num = maior_num = num

    elif num < menor_num:
        menor_num = num

    elif num     > maior_num:
        maior_num = num
    
    continuar = input('Deseja continuar? [s/n] ').lower()

print(f'O maior numero foi {maior_num}')
print(f'O menor numero foi {menor_num}')
print(f'Foram inseridos {cont} números, a media entre todos eles foi de {soma/cont}')