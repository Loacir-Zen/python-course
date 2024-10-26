emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"

email = input('Entre com email: ')

if email in emails_spam:
    print("É spam")
else:
    print('Não é spam')