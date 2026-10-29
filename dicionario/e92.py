from datetime import datetime

pessoa = {}

pessoa['Nome'] = input('Nome: ')

#Pega o ano que o usuario nasceu e calcula a idade somente com base no ano, tambem valida para inserir somente idade entre 100 anos e maior que 16
while True:
    try:
        ano_nascimento = int(input('Digite o ano de nascimento: '))
        if  1926 <= ano_nascimento <= 2010:
            ano_atual = datetime.now().year
            pessoa['Idade'] = ano_atual - ano_nascimento
            break
        else:
            print('data de nascimento invalida ou nao permitida.')
        
    except ValueError:
        print('Insira somente numeros')

pessoa['CTPS'] = int(input('Insira o numero da sua Carteira de Trabalho: [se nao tiver insira 0] '))

if pessoa['CTPS'] != 0:
    pessoa['Salario'] = float(input('Insira seu salário: '))
    pessoa['Ano_contrat'] = int(input('Insira o ano em que você foi contratado: '))

    pessoa['Idade_aposent'] = (pessoa['Ano_contrat'] - ano_nascimento) + 35

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

