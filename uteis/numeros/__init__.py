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
