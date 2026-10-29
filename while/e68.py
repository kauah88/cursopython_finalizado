import random
n_comp = random.randint(1,10)
contVit = 0
imp_par = ''

while True:
    print('-'*70)

    #validacao do input I ou P

    while True:

        imp_par = input('Voce quer impar ou par? [I/P] ').lower()

        if imp_par in ['i', 'p']:
            break
        else:
            print('Inisira somente [I/P]')


    n_jogador = int(input('Diga um valor: '))
    print('-'*70)
    soma_num = n_comp + n_jogador 

    if soma_num % 2 == 0:
        result_imp_par = 'PAR'
    else:
        result_imp_par = 'IMPAR'

    print(f'Voce jogou {n_jogador} e o computador jogou {n_comp} o total de: {soma_num}. Deu {result_imp_par}')
    print('-'*70)


    if imp_par == result_imp_par[0].lower() :
        print(f'VOCE VENCEU!!')
        contVit +=1

    else:
        print(f'Voce perdeu :(\nO numero de vitorias foi de {contVit}')
        break
