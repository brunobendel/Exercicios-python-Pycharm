from Ex115.lib.interface import *
from time import sleep

arq = 'Nomes.txt'

if not ArqExiste(arq):
    CriarArquivo(arq)
while True:
    resp = menu (['Ver Pessoas Cadastradas','Cadastrar Pessoas','Sair do Siatema'])
    if resp == 1:
        LerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome =str(input('Nome: '))
        idade =leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do Sistema.')
        break
    else:
        print('\033[31mERRO: Digite uma Opção valida.\033[m')
    sleep(1)

