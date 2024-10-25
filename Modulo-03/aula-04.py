"""
meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 280000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
else: 
    bonus = 0


print(f'O bonus do funcionário foi de {bonus}')
"""
meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 8000
vendas_loja = 200000

nota_funcionario = 9
meta_nota = 9 

if nota_funcionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
    bonus = 0.03 * vendas_funcionario
    print(f'Bonus do funcionário foi de {bonus}')
else:
    print('O funcionário não recebeu bonus')