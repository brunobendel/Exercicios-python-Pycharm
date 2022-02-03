valores = list()

while True:

    n = int(input('Digite um valor: '))

    if n in valores:

        print('Esse valor não foi adicionado a lista')

    elif n not in valores:
        valores.append(n)
    v = str(input('Deseja continuar? S/N: ')).upper().strip()

    if v == 'N':
        break

valores.sort() # coloca em ordem crescente
print(f'Você digitou os valores {valores}.')

