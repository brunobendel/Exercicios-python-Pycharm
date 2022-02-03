import math
Ex=('Desafio 18')
print('{:=^40}'.format(Ex))
num=int(input('digite um angulo: '))
c=math.cos(math.radians(num))
s=math.sin(math.radians(num))
t=math.tan(math.radians(num))
print('O valor do seno de {} é {:.3f}\nO valor do cosseno de {} é {:.3f}\nO valor da tangente de {} é {:.3f}\n'.format(num,s,num,c,num,t))

