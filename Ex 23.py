n = int(input('Digite um numero de 0 a 9999: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analizando Esse numero {}'.format(n))
print('unidades {} '.format(u))
print('dezenas {}'.format(d))
print('centenas {} '.format(c))
print('milhares {}'.format(m))
