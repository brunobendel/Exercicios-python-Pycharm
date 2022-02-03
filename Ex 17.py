import math
Ex=('Desafio 17')
print('{:=^40}'.format(Ex))
adj=int(input('digite o valor do cateto adjacente: '))
op=int(input('digite o valor do cateto oposto: '))
hip= math.sqrt((adj ** 2) + (op ** 2))
print('o valor da Himpotenusa é:{}'.format(hip))

