meta = 0.05
taxa = 0
redimento = 0.21

if redimento > meta:
    if redimento > 0.20 :
        taxa = 0.04
        print(f'A taxa foi de {taxa}')
    else:
        taxa = 0.02
        print(f'A taxa foi de {taxa}')
else: 
    taxa = 0
    print(f'A taxa foi de {taxa}')
