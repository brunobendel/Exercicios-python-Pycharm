from random import randint
from time import sleep
palpite = []
lista = []
total = 0
quant = int(input('Digite a quantidade de jogos que deseja fazer:'))
while total < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in palpite:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    palpite.append(lista[:])
    lista.clear()
    total += 1
for f, v in enumerate(palpite):
    print(f'jogos {f+1}: {v} ')
    sleep(1)
