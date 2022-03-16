def linha(tam=42):
    return '~='*tam

def cabeçalho(txt):
    print(linha(21))
    print(txt.center(42))
    print(linha(21))

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um numero inteiro.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO Usuario preferiu não digitar o numero.\033[m')
            return 0
        else:
            return n


def menu(lista):
    cabeçalho('Menu Principal')
    c =1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha(21))
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc

def LerArquivo(nome):
    try :
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabeçalho('Pessoas cadastradas')
        print(a.read())
def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um Erro na criação de uma arquivo')
    else:
        print(f'O arquivo {nome} foi criado com sucesso.')
def ArqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
