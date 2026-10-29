while True:
    try:
        numero1 = int(input('Digite o 1° numero: '))
        numero2 = int(input('Digite o 2° numero: '))
        print('----------------------------------')
        print('Qual operação deseja realizar?')
        print('[1] Soma')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos numeros')
        print('[5] Sair do programa?')
        print('----------------------------------')
        break
    except ValueError:
        print('Insira somente numeros inteiros!')
        
while True:

        while True:
            try:
                resposta = int(input('>> '))
                print('----------------------------------')
                break
            except ValueError:
                print('Opção invalida! tente novamente.')

        while resposta != 5:
            if resposta == 1:
                print(f'{numero1} + {numero2} = {numero1+numero2}')
                break

            if resposta == 2:
                print(f'{numero1} * {numero2} = {numero1*numero2}')
                break
            if resposta == 3:
                if numero1 > numero2:
                    maior_numero = numero1 
                    print(f'O maior numero e o {maior_numero}')
                    break

                elif numero1 < numero2:
                    maior_numero = numero2
                    print(f'O maior numero e o {maior_numero}')
                    break

                else:
                    print('Os numeros sao iguais')
                    break

            if resposta == 4:
                print('Digite os novos numeros')
                numero1 = int(input('Digite o 1° numero: '))
                numero2 = int(input('Digite o 2° numero: '))
                break

        if resposta == 5:
                print('Fim do programa, Obrigado!')
                break
        print('----------------------------------')
        print('Qual operação deseja realizar?')    
        print('[1] Soma')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos numeros')
        print('[5] Sair do programa?')
        print('----------------------------------')
        