tipo_combustivel = input('Informe o tipo do combustível:')
qtde_combustivel = float(input('Entre com a quantidade de combustível:'))

if tipo_combustivel == 'Álcool':
    preco_sem_desconto = qtde_combustivel * 1.9
    if qtde_combustivel <= 20:
        taxa_desconto = 0.03
    elif qtde_combustivel > 20:
        taxa_desconto = 0.05
elif tipo_combustivel == 'Gasolina':
    preco_sem_desconto = qtde_combustivel * 2.5
    if qtde_combustivel <= 20:
        taxa_desconto = 0.04
    elif qtde_combustivel > 20:
        taxa_desconto = 0.06

preco_liquido = preco_sem_desconto - (preco_sem_desconto * taxa_desconto)

print(f'Combustível: {tipo_combustivel}')
print(f'Qtde de Computível: {qtde_combustivel}')
print(f'O valor sem desconto: {preco_sem_desconto} ')
print(f'Taxa de desconto: {taxa_desconto} ')
print(f'Preço Líquido: {preco_liquido} ')

