primeira_parcial = float(input('Entre com a primeira nota parcial: '))
segunda_parcial = float(input('Entre com a segunda nota parcial: '))


media_nota = (primeira_parcial + segunda_parcial) / 2

if media_nota >= 9 :
    conceito = 'A'
elif media_nota >= 7.5 and media_nota < 9:
    conceito = 'B'
elif media_nota >= 6 and media_nota < 7.5:
    conceito = 'C'
elif media_nota >= 4 and media_nota < 6:
    conceito = 'D'
elif media_nota >= 0 and media_nota < 4:
    conceito = 'E'

print(f'A média foi {media_nota} - {conceito}') 

