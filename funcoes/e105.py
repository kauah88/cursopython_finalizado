def notas (*nota , sit = False):    
    dict_notas = {}
    soma = maior = menor = 0
    dict_notas['total'] = len(nota)

    for i, v in enumerate(nota):
        if i == 0:
            dict_notas['menor']= v
        else:
            if v > maior:
                dict_notas['maior'] = v
                
            elif v < menor:
                dict_notas['menor'] = v

        soma += v
    dict_notas['media'] = soma/dict_notas['total']

    if sit:
        if dict_notas['media'] > 8:
            dict_notas['situação'] = 'Ótima'

        elif 8 >= dict_notas['media'] >= 6 :
            dict_notas['situação'] = 'Boa'

        else:
            dict_notas['situação'] = 'Reprovado'

    return dict_notas

print(notas(3.5, 10, 6.5, sit=True))
