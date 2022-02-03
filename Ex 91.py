from random import randint
from time import sleep
dicionario = {'Jogador 1':randint(1,6),
              'Jogador 2':randint(1,6),
              'Jogador 3':randint(1,6),
              'Jogador 4':randint(1,6)}
print('   Jogo de dados    ')
print('-='*30)
for n, j in dicionario.items():
    print(f'{n} tirou {j} no dado.')
    sleep(1)


