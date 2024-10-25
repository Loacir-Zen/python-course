meta = 20000
bonus = 0

valor_vendas = float(input('Entre com total de vendas realizado pelo vendedor: '))


if valor_vendas > meta * 2:
    bonus = 0.07 * valor_vendas
elif valor_vendas > meta :
    bonus = 0.03 * valor_vendas
else: 
    bonus = 0 * valor_vendas

print(f"O total de vendas foi {valor_vendas}, a meta era {meta}, portanto o bonus foi de {bonus}") 