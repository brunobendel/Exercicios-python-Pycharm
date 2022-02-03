valores = []

while True:

    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
    v = str(input('Deseja continuar? S/N: ')).upper().strip()

    if v == 'N':
        break

print('-='* 30)

if 5 in valores:
    print(f'O Valor 5 está na lista')
else:
    print(f'O Valor 5 não está na lista')

valores.sort(reverse=True)

print(f'Você digitou os valores {valores}')
print(f'A lista tem {len(valores)} elementos.')
