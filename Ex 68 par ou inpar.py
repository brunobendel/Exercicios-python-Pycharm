from random import randint
vitoria = 0
while True:
    maq = randint(0, 10)
    num = int(input('Digite  uma numero: '))
    tipo = ' '
    total = num + maq
    while tipo not in 'IiPp':
        tipo = str(input('Par ou inpar?')).strip()[0].upper()
    print(f'Voce escolheu {num} e o PC escolheu {maq} e o total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vitoria += 1
        else:
            print('Game Over! Você perdeu.')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            vitoria += 1
        else:
            print('Game Over! Você perdeu.')
            break
print(f'Você ganhou {vitoria} vezes.')






