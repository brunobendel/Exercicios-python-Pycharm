cont = soma = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if  num >maior:
            maior = num
        if num < menor :
            menor = num
    resp = str(input('Deseja continuar S/N ? ')).upper().strip()[0]
media = soma/cont
print(f'Soma= {soma} Média={media} foi digitado {cont} números.\nmaior numero é {maior} e o menor é {menor}')