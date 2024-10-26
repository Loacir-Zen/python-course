num_x = float(input('Entre com o numero para X: '))
num_y = float(input('Entre com o numero para Y: '))

maior_numero = num_x

if num_y > maior_numero:
    maior_numero = num_y

print(f'O maior numero informado é { maior_numero }')