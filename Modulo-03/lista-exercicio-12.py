qtde_horas = float(input('Entre com a quantidade de horas: '))
valor_hora = float(input('Entre com o valor da hora: '))
salario_mes = qtde_horas * valor_hora


if salario_mes <= 900:
    ir = 0
elif salario_mes <= 1500:
    ir = 0.05
elif salario_mes <= 2500:
    ir = 0.1
else:
    ir = 0.2   

desconto_ir = salario_mes * ir
desconto_inss = salario_mes * 0.10
fgts = salario_mes * 0.11
total_descontos = desconto_ir + desconto_inss  + ir


print(f'Salário Bruto: ({valor_hora} * {qtde_horas}): {salario_mes}')
print(f'(-) IR ({ir}%): {desconto_ir}')
print(f'(-) INSS (10%): {desconto_inss}')
print(f'FGTS (11%): {fgts}')
print(f'Total de descontos: {total_descontos}')
print(f'Salario líquido: {salario_mes - total_descontos}')
           








