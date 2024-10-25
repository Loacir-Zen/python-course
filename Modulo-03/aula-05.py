"""
faturamento = input('Qual foi o faturamento da loja nesse mês? ')
custo = input('Qual foi o custo da loja nesse mês? ')

if faturamento == '' or custo =='':
    print('Preencha o faturamento e o custo corretamente')
else:
    lucro = int(faturamento) - int(custo)
    print(f'O lucro da loja doi de {lucro} reais')
"""
faturamento = input('Qual foi o faturamento da loja nesse mês? ')
custo = input('Qual foi o custo da loja nesse mês? ')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print(f'O lucro da loja doi de {lucro} reais')
else: 
    print('Preecha o faturamento e o custo corretamente')
