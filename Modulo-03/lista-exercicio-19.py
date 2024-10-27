p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

resposta = input("Telefonou para a vítima? ")
if resposta == 'sim':
    p1 = 1

resposta = input("Esteve no local do crime? ")
if resposta == 'sim':
    p2 = 1

resposta = input("Mora perto da vítima? ")
if resposta == 'sim':
    p3 = 1

resposta = input("Devia para a vítima? ")
if resposta == 'sim':
    p4 = 1

resposta = input("Já trabalhou com a vítima? ")
if resposta == 'sim':
    p5 = 1

total = (p1 + p2 + p3 + p4 +p5)

if total == 5: 
    print('Assassino')
elif total == 4 or total == 3:
    print('Cúmplice')
elif total == 2:
    print('Suspeito')
else: 
    print('Inocente')
