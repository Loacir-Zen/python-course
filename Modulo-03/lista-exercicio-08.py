produto_um = input('Informe o Primeiro Produto: ')
preco_produto_um = float(input('Entre com o valor do produto um: '))

produto_dois = input('Informe o Segundo Produto: ')
preco_produto_dois = float(input('Entre com o valor do produto dois: '))

produto_tres = input('Informe o Terceiro Produto: ')
preco_produto_tres = float(input('Entre com o valor do produto três: '))

produto_vencedor = produto_tres

if preco_produto_um < preco_produto_dois and preco_produto_um < preco_produto_tres:
    produto_vencedor = produto_um
elif preco_produto_dois < preco_produto_um and preco_produto_dois < preco_produto_tres:
    produto_vencedor = produto_dois

print(f'O produto que você deve levar é {produto_vencedor}')
