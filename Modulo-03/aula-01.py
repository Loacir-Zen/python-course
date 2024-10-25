meta = 50000

qtde_vendidas = int(input('Entre com a quantidade vendida: '))

if qtde_vendidas >= meta:
    print(f'Batemos a meta, vedemos {qtde_vendidas} unidades')
else: 
    print(f'Não batemos a meta, vedemos apenas {qtde_vendidas} unidade')

