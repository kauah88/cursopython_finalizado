def metade (preco):
    return  preco / 2

def dobro (preco):
    return preco * 2
    
def aumentar(preco, valor_aumentar):
    porcentagem = (valor_aumentar / 100) + 1
    return preco * porcentagem

def diminuir (preco, valor_diminuir):
    porcentagem = valor_diminuir / 100
    return preco * porcentagem

print(diminuir(150, 50))
print(aumentar(100, 50))