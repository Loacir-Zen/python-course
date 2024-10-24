""" 
faturamento = 1000
custo = 400

lucro = faturamento - custo

# com format 
print("O faturamento foi de {} e o lucro de {}" .format(faturamento, lucro))

# com f-string
print(f"O faturamento foi de {faturamento} e o lucro de {lucro}")

"""

faturamento = float(input("Insira o faturamento: "))
custo = float(input("Insira o custo: "))

lucro = faturamento - custo 
print(lucro)

