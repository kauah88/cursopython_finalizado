pt = int(input("Qual o primeiro Termo: "))
razao = int(input("Qual a razao da P.A?: "))
cont = 0
tam_loop = 10
termos_novos = 1

while termos_novos != 0:
    while cont < tam_loop:
        print(f'{pt} ➝ ', end =' ')
        pt += razao
        cont+=1

    print('PAUSA')
    
    termos_novos = int(input("Quantos termos a mais deseja ver (0 para cancelar)  "))
    tam_loop += termos_novos

print(f'Progressão finalizada com {cont} termos mostrados')