area = float(input('Entre com a quantidade de áreas quadradas: '))

litros_tinta = area / 3 
latas = litros_tinta / 18
preco = latas * 80

print(f'Serão necessárias {latas} latas, custando R$ {preco} no total')