salario = float(input('Entre com o valor do salário: '))
aumento_salario = 0
percentual_aumento = 0

if salario < 280:
    percentual_aumento = 0.20
    aumento_salario = salario * percentual_aumento
elif salario >= 280 and salario < 700:
    percentual_aumento = 0.15
    aumento_salario = salario * percentual_aumento
elif salario >= 700 and salario < 1500:
    percentual_aumento = 0.10
    aumento_salario = salario * percentual_aumento
else:
    percentual_aumento = 0.10
    aumento_salario = salario * percentual_aumento

print(f'Salario antes do rejuste {salario}')
print(f'Percentual de aumento aplicado {percentual_aumento}')
print(f'O valor do aumento {aumento_salario}')
print(f'Novo salário {salario + aumento_salario}')
