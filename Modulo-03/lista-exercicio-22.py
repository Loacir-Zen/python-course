tipo = input('Informe o tipo da carne: ')
quantidade = float(input('Informe a quantidade de carne: '))
pagamento = input('Escolha a forma de pagamento (C - Cartão Tabajara/D - Dinheiro): ')

if tipo == 'File Duplo' and quantidade > 5:
    total = 5.8 * quantidade
elif tipo == 'File Duplo' and quantidade <= 5:
    total = 4.9 * quantidade
elif tipo == 'Alcatra' and quantidade > 5:
    total = 6.8 * quantidade
elif tipo == 'Alcatra' and quantidade <= 5:
    total = 5.9 * quantidade
elif tipo == 'Picanha' and quantidade > 5:
    total = 7.8 * quantidade
elif tipo == 'Picanha' and quantidade <= 5:
    total = 6.9 * quantidade
    
print('--- CUPOM FISCAL ---')
print('Tipo da carne:', tipo)
print('Quantidade:', quantidade, 'kg')
print('Preço total: R$', total)
print('Forma de pagamento:', pagamento)

desconto = 0.05 * total if pagamento == 'C' else 0

print('Desconto: R$', desconto)
print('Valor a pagar: R$', total - desconto)