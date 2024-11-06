produtos = ['TV', 'Celular', 'Tablet', 'Mouse', 'Teclado', 'Geladeira', 'Forno']
estoque = [100, 150, 100, 120, 70, 90, 80]

i = produtos.index('Geladeira')
qtde_estoque = estoque[i]
print(i)
print(produtos[i])
print(qtde_estoque)

produto = input('Insira o nome do produto em letra minúscula: ')
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque= estoque[i]
    print(f'Temos {qtde_estoque} de produto {produto} no estoque')
else: 
    print(f'{produto} não existe no estoque')