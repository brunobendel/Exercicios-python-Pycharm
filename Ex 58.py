from random import randint
n = int(input('olá sou seu computado...\nEstou pensando um um numero entre 0 e 100\nTente acertar:'))
o = randint(0,100)
t = 1
while n != o :
    t += 1
    if n < o:
        n = int(input(f'MAIOR que {n} tenta de novo:'))  # print(f'{n}')
    elif n > o:
        n = int(input(f'MENOR que {n} tenta de novo:'))
print(f'Parabens voce acertou em {t} tentativas')

