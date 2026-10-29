tupla = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in tupla:
    print(f'As Vogais em {palavra.upper()} sao:', end = ' ' )
    for letra in palavra:
        if letra in ('a', 'e', 'i', 'o', 'u'):
            print(letra, end = ' ')
    print()