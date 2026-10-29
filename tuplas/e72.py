contagem = (
    "zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", 
    "onze", "doze", "treze", "quatorze", "quinze", 
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)


while True:
    try:
        numero = int(input('Digite um numero de 0 a 20: '))
        if numero  in range(21):
            break
        else:
            print('Numero invalido digite somente numeros entre 0 e 20')
    except ValueError:
        print('Insira somente numeros')

print(f'Você digitou o numero {contagem[numero]}')
