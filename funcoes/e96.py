def area(largura, comprimento):
    area = largura * comprimento
    print(f'A area do seu terreno {largura} x {comprimento} e de {area}m²')

largura = float(input('Qual a largura do seu terreno? (m)'))
comprimento = float(input('Qual o comprimento do seu terreno? (m)'))

area(largura, comprimento)