from Ex115.lib.interface import *
from time import sleep

while True:
    resp = menu (['Ver Pessoas Cadastradas','Cadastrar Pessoas','Sair do Siatema'])
    if resp == 1:
        cabeçalho('Opção 1')
    elif resp == 2:
        cabeçalho('Opção 2')
    elif resp == 3:
        cabeçalho('Saindo do Sistema.')
        break
    else:
        print('\033[31mERRO: Digite uma Opção valida.\033[m')
    sleep(1)

