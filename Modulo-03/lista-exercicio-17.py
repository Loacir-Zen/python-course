limite_peso = 50
peso_excedente = 0

peso_pescado = float(input('Entre com o total do peso pescado: '))

if peso_pescado > limite_peso:
    peso_excedente = peso_pescado - limite_peso

multa = peso_excedente * 4

print(f'O peso pescado foi {peso_pescado} kg, logo o peso excedente foi {peso_excedente} kg, portanto a multa será de R$ {multa}')


