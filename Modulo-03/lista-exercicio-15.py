ano = int(input('Informe o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano é bissexto.')
else:
    print('Não é um ano bissexto.')