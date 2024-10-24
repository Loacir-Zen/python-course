tamanho = float(input('Entre com o tamanho do arquivo em MB: '))
velocidade = float(input('Entre com a velocidade da conexão em Mbps: '))

tamanho_megabits = tamanho * 8
tempo = tamanho_megabits / velocidade
tempo_minutos = tempo / 60

print(f'O tempo de download é de {tempo_minutos} minutos')