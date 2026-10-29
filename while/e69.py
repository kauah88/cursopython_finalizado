idade = 0
sexo = ''
continuar = 's'
cont_maior_idade = 0
cont_masc = 0
cont_idade_F = 0

while continuar == 's':

    while True:
        try:
            idade = int(input('Qual a idade da pessoa? ') )
            if idade > 0:
                break
            else:
                print('Idade Invalida!')
        except ValueError:
            print('Insira somente numeros')
            
    while True:
        sexo = input('Qual o sexo da pessoa? [m/f]').lower().strip()
        if sexo  in ['m', 'f']:
            break
        else:
            print('Insira somente "m" para masculino e "f" para feminino')
            
    while True:
        continuar = input('Deseja continuar cadastrando pessoas? [s/n]').lower().strip()
        if continuar in ['s', 'n']:
            break
        else:
            print('Insira "s" para sim e "n" para não')

    if idade >=18:
        cont_maior_idade+=1

    if sexo == 'm':
        cont_masc+=1

    if sexo == 'f' and idade < 20:
        cont_idade_F+=1

print(f'Foram cadastrados {cont_maior_idade} pessoas maiores de idade')
print(f'Foram cadastrados {cont_masc} pessoas do sexo Masculino')
print(f'Foram cadastradas {cont_idade_F} mulheres com menos de 20 anos')