primeiro_orcamento = float(input('Entre com o orçamento da Empresa X: '))
segundo_orcamento = float(input('Entre com o orçamento da Empresa Y: '))
terceiro_orcamento = float(input('Entre com o orçamento da Empresa Z: '))

maior_orcamento = 0

if primeiro_orcamento > segundo_orcamento and primeiro_orcamento > terceiro_orcamento:
    maior_orcamento = primeiro_orcamento
elif segundo_orcamento > primeiro_orcamento and segundo_orcamento > terceiro_orcamento:
    maior_orcamento = segundo_orcamento
else: 
    maior_orcamento = terceiro_orcamento

print(f'O maior orçamento foi {maior_orcamento}')