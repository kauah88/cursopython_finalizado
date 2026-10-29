status = {}

status['Nome'] = input('Nome: ')

while True:
    status['Media'] = float(input(f'Media de {status["Nome"]}: '))

    if status['Media'] > 10:
        print('Nota Invalida! A media maxima e de 10.0 pts')
    else:
        break

if status['Media'] >= 7: 
    status['Situação'] = 'Aprovado'
else:
    status['Situação'] = 'Reprovado'

for c, v in status.items():
    print(f'{c} igual a {v}')