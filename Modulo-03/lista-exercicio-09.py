numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))
numero3 = float(input('Informe o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    print('O maior número é', numero1)
    if numero2 > numero3:
        print('O segundo maior número é', numero2)
        print('O terceiro maior número é', numero3)
    else:
        print('O segundo maior número é', numero3)
        print('O terceiro maior número é', numero2)
elif numero2 > numero1 and numero2 > numero3:
    print('O maior número é', numero2)
    if numero1 > numero3:
        print('O segundo maior número é', numero1)
        print('O terceiro maior número é', numero3)
    else:
        print('O segundo maior número é', numero3)
        print('O terceiro maior número é', numero1)
elif numero3 > numero1 and numero3 > numero2:
    print('O maior número é', numero3)
    if numero1 > numero2:
        print('O segundo maior número é', numero1)
        print('O terceiro maior número é', numero2)
    else:
        print('O segundo maior número é', numero2)
        print('O terceiro maior número é', numero1)