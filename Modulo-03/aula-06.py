produto = input('Qual é o produto: ')
categoria = input('Qual é a categoria do produto: ')
qtde_produto = input('Qual é a quantidade atual do produto: ')

if produto and categoria and qtde_produto: 
    qtde_produto = int(qtde_produto)
    if categoria == 'bebidas' :
        if qtde_produto < 75:
            print(f'Solicitar {categoria} a equipe de compras, temos apenas {qtde_produto} em estoque')
    elif categoria == 'alimentos' :
        if qtde_produto < 50:
            print(f'Solicitar {categoria} a equipe de compras, temos apenas {qtde_produto} em estoque')
    elif categoria == 'limpeza' :
        if qtde_produto < 30:
            print(f'Solicitar {categoria} a equipe de compras, temos apenas {qtde_produto} em estoque')
    else: 
        print("Categoria não existe")
                 
else:
    print('Preencha os dados corretamente')