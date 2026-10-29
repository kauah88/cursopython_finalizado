peso_pessoas = []
continuar = 's'
maior_peso = menor_peso = 0 

while continuar in 's':
    dados = []

    nome = input('Insira o nome: ')
    dados.append(nome)

    while True:
        try:
            peso = float(input('Insira o peso: '))
            dados.append(peso)
            break

        except ValueError:
            print('Insira somente numeros!')

    if menor_peso == 0:
        menor_peso = peso
        maior_peso = peso

    else:
        if peso >= maior_peso:
            maior_peso = peso

        elif peso <= menor_peso:
            menor_peso = peso

    peso_pessoas.append(dados[:])
    dados.clear()
    
    while True:
        continuar = input('Deseja continuar? [s/n] ').lower()
        if continuar in ['s', 'n']:
            break
        else:
            print('Insira somente "s" para sim e "n" para não ')


print(f'\nForam cadastradas {len(peso_pessoas)} pessoas na lista')
pesados = []
leves = []

for p in peso_pessoas:
    if p[1] == maior_peso:
        pesados.append(p[0])

    if p[1] == menor_peso:
        leves.append(p[0])

print(f'O maior peso foi {maior_peso} de ', end = '')
for i, p in enumerate(pesados):
    if i < len(pesados) - 1:
        print(f'{p} e ', end = '')
    else:
        print(f'{p}', end = '')
print()

print(f'O menor peso foi {menor_peso} de ', end = '')
for i, p in enumerate(leves):
    if i < len(leves) - 1:
        print(f'{p} e ', end = '')
    else:
        print(f'{p}', end = '')
