n = int(input('Digite um numero pra saber se ele é primo:'))
t = 0
for c in range (1,n+1):
    if n % c == 0: # Se o numero for divisivel
        print('\033[33m',end=' ') # Amarelo
        t= t+1 #ou t+=1
    else:
        print('\033[31m',end=' ') # vermelho
    print(c, end=' ')

print('\n\033[mO numero {} foi divisivel {} vezes'.format(n,t))
if t == 2:
    print('Esse numero é primo')
else:
    print('Esse numero não é primo')

