Ex=('Progreção aritimética')
print('{:=^40}'.format(Ex))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        cont += 1
        termo += razao
    print('Pausa')
    mais = int(input('Digite outra razão ou digite 0: '))
print(f'{total} Total de razão mostrada')
