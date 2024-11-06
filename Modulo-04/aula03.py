produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'Apple Watch', 'Mac Book', 'Airpods']
print(produtos)
#produtos[2] = 'iphone 11'

produtos.append('iphone 11')

print(produtos)

#adicionar o iphone 11

#remover o iphone x

#produtos.remove('iphone x')

try: 
    produtos.remove('iphonex')
    print(produtos)
except: 
    print('iphonex não existe na lista de produtos')

item_removido = produtos.pop(2)
print(f'Removemos o {item_removido} da lista')