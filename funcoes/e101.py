from datetime import date


def votar (ano_nasci):
    ano_atual = date.today().year
    idade = ano_atual - ano_nasci
    try :
        if 18 < idade < 64:
            return (f'com {idade} anos tem que votar')
        elif idade < 16:
            return (f'com {idade} anos não vota')
        else:
            return (f'com {idade} anos o voto opcional')
    except ValueError:
        print('Insira somente numeros inteiros')


ano_nascimento = int(input('Em que ano voce nasceu? '))

print(votar(ano_nascimento))
    
    