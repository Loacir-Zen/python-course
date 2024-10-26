primeira_nota = float(input('Entre com a primeira nota: '))
segunda_nota = float(input('Entre com a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

if media >= 7 and media < 10:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com Distinção')
else:
    print('Valor incorreto')
