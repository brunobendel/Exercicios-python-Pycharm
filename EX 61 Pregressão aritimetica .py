Ex=('Progreção aritimética')
print('{:=^40}'.format(Ex))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
termo = primeiro
while cont <= 11 :
    print(f'{termo} > ', end='')
    cont += 1
    termo += razao
print('fim')
