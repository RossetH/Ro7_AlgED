ano = int(input('Digite um ano para descobrir se ele é bissexto:\n'))

if ano % 4 == 0:
    if ano % 100 != 0:
        print('\n O ano digitado é um ano bissexto')
    elif ano % 400 == 0:
            print('\n O ano digitado é um ano bissexto')
    else:
        print('\n O ano digitado não é um ano bissexto')
else:
    print('\n O ano digitado não é um ano bissexto\n')