x = int(input('Digite um numero qualquer e mostre seu fatorial: '))
c = x
f = 1
print(f'Calculando {x}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f = f * c  # f *= c
    c -= 1
print('{}'.format(f))
