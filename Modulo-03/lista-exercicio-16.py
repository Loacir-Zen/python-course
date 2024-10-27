primeira_parcial = float(input('Entre com a primeira nota: '))
segunda_parcial = float(input('Entre com a segunda nota: '))
terceira_parcial = float(input('Entre com a terceira nota: '))

media_nota = (primeira_parcial + segunda_parcial + terceira_parcial) / 3

if media_nota == 10:
    print('Aprovado com distinção')
elif media_nota > 7:
    print('Aprovado')
else: 
    print('Reprovado')
