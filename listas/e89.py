lista_notas = [] #listas das notas
lista_dados = [] #lista de todos os dados dos alunus individualmente (nome e nota)
lista_alunos_geral = [] #lista com todos os alunos
continuar = 's'
nome = ''
soma = nota = 0

while continuar in 's':
    #n vou fazer validação para o nome mas deveria
    nome = input('Insira o nome do aluno: ')
    lista_dados.append(nome)

    cont_notas = 0 # contador para inserir somente duas notas, nao usei o for se nao nao daria para fazer a validação do jeito que eu queria
    while cont_notas  != 2:
        try:
            nota = float(input(f'Insira a nota {cont_notas+1} de {nome}: '))

            if nota <= 10: #limita a nota inserida a 10
                lista_notas.append(nota)
                cont_notas+=1
                soma += nota #cria a variavel que vai somar a nota acumulada do aluno para calcular a media 
            else:
                print('As notas podem ser no maximo ate 10.0 pontos!')
    
        except ValueError:
            print('Insira somente numeros')

    
    media = soma / 2
    #media entra na lista de notas como o terceiro elemento(eu nao quis fazer uma 4 sub lista)
    lista_notas.append(media)


    #reseta a variavel para o calculo do proximo aluno, se nao fizer isso a media se acumula com as dos anteriores
    soma = 0
    
    #adicionando as sublistas a lista principal
    lista_dados.append(lista_notas[:])
    lista_alunos_geral.append(lista_dados[:])

    lista_dados.clear()
    lista_notas.clear()

    continuar = input('Deseja continuar? [s/n]')

print('-'*25)
print('No. Nome    Media')
for i, v in enumerate(lista_alunos_geral):
    print(f'{i+1}  {v[0]}     {v[1][2]}')
print('-'*25)

while True:
    mostrar = int(input(f'Mostrar notas de qual aluno? [0 para sair] ')) - 1

    if mostrar == -1: #interrompe o laço com -1 pq eu estou tirando 1 da variavel mostrar pq eu estou adicionando 1 somente na visualização do indice (gambiarra)
        break

    print(f'Notas de {lista_alunos_geral[mostrar][0]} foram {lista_alunos_geral[mostrar][1][:2]}')
    print('-'*25)


