num_horas = float(input('Entre com a quantidade de horas trabalhada no mês: '))
valor_hora = float(input('Entre com valo da hora trabalhada: '))

salario_bruto = num_horas * valor_hora
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100 
sindicato =  (salario_bruto * 5) / 100 
total_desconto = ir + inss + sindicato
salario_liquido = salario_bruto - total_desconto

print(f'Salario Bruto foi {salario_bruto}')
print(f'O desconto do IR foi {ir}')
print(f'O desconto do INSS foi {inss}')
print(f'O desconto do Sindicato foi {sindicato}')
print(f'O salário liquido foi {salario_liquido}')