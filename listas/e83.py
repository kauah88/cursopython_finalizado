cont_parent_aberto = 0
cont_parent_fechado = 0

expressao = input('Digite sua expressao: ')

for c in expressao:
    if c == '(':
        cont_parent_aberto+=1
    if c == ')':
        cont_parent_fechado+=1

if cont_parent_aberto == cont_parent_fechado:
    print('Expressao valida!')
else:
    print('Expressao invalida')