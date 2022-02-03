from random import randint
from time import sleep
com = randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar!!!')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei:'))
print('Processando')
sleep(3)
if com == jogador:
    print('\033[32mParabens você acertou')
    sleep(3)
else:
    print('se fodeu eu pensei em : {}'.format(com))
    sleep(3)
