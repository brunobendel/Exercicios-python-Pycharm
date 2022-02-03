valores = []
pares = []
impares = []

while True:

    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
    v = str(input('Deseja continuar? S/N: ')).upper().strip()

    if n % 2 == 0:
        pares.append(n)

    if n % 2 == 1:
        impares.append(n)

    if v == 'N':
        break

print('-='* 30)


valores.sort()

print(f'Você digitou os valores na lista completa: {valores}')
print(f'A lista tem {len(valores)} elementos.')
print(f'Os valores pares são {pares}')
print(f'Os valores impares são {impares}')


































