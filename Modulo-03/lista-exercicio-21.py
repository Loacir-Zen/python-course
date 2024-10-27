tipo = input('Informe o tipo de combustível: ')
quantidade = float(input('Informe a quantidade de combustível: '))

if tipo == 'A' and quantidade <= 20:
    total = (1.9 * quantidade) * 0.97
elif tipo == 'A' and quantidade > 20:
    total = (1.9 * quantidade) * 0.95
elif tipo == 'G' and quantidade <= 20:
    total = (2.5 * quantidade) * 0.96
elif tipo == 'G' and quantidade > 20:
    total = (2.5 * quantidade) * 0.94

print('Total a pagar: R$', total)