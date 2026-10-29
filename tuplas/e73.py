brasileirao_2026 = (
    "Palmeiras",          # 1º
    "Flamengo",           # 2º
    "Athletico-PR",       # 3º
    "Fluminense",         # 4º
    "Cruzeiro",           # 5º
    "Bahia",              # 6º
    "Bragantino",# 7º
    "Coritiba",           # 8º
    "Atlético-MG",        # 9º
    "Corinthians",        # 10º
    "Botafogo",           # 11º
    "Vitória",            # 12º
    "São Paulo",          # 13º
    "Santos",             # 14º
    "Grêmio",             # 15º
    "Internacional",      # 16º
    "Mirassol",           # 17º
    "Remo",               # 18º
    "Vasco",              # 19º
    "Chapecoense"         # 20º
    
)

print(f'Esses sao os cinco primeiros colocados do campeonato brasileiro: ')

for i in range(len(brasileirao_2026),):
    print(f'{i+1}° {brasileirao_2026[i]}')
    if i == 4:
        break
print('\nEsses sao os quatro ultimos:')

i = len(brasileirao_2026) - 3 #len retorna o tamanho da string mas a posição começa em 0, se eu tirar menos 3 ele funciona se nao ele nao fucniona a posição fica 19°
for times in brasileirao_2026[-4:]:
    print(f'{i}° {times}')
    i+=1

# times_ordem_alf = sorted(brasileirao_2026)
# print('Essa e a tabela dos times em ordem alfabetica: ')
# for times in times_ordem_alf:
#     print(times)
cont = 0

while True:
    time = input('Qual time voce quer saber a posição no compeonato? ').capitalize()
    if time in brasileirao_2026:
        break
    else:
        print(f'o clube {time} nao esta no campeonato')

for i in range(len(brasileirao_2026)):
    cont+=1
    if brasileirao_2026[i] == time:
        break

print(f'O {time} esta na {cont}° posição')