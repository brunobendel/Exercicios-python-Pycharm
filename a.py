
while True:
    num = int(input('Digite  uma numero: ')
    maq = randint (0,10)
    tipo = ' '
    total = num + maq
    while tipo is not in 'IiPp':
        tipo = str(input('Par ou inpar?')).strip()[0]
    print(f'Voce escolheu {num} e o PC escolheu {maq} e o total foi {total}')