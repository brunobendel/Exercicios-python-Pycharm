def fatorial(n):
    f = 1
    for c in range (1 , n+1):
        f *= c
    return f


def dobro(n):
    d = n* 2
    return d


def contador(i=0,f=0,p=1):
    c = i
    while c<=f:
        print(f'{c}', end=" ")
        c += p
    print('Fim!')


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

def leiafloat (msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um numero real.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO Usuario preferiu não digitar o numero.\033[m')
            return 0
        else:
            return n
