matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = mai = scol = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para matriz {l} e {c}:'))
print('xX'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            par = matriz[l][c] + par # ou par += matriz[l][c]

    print()
print(f'Soma dos pares é igual a {par}')

for l in range(0,3):
    scol += matriz[l][2]
print(f'Soma da coluna 2 é : {scol}')

for c in range(0,3):
    if c == 0:
        mai =matriz[1][c]
    elif matriz[1][c]> mai:
        mai = matriz[1][c]
print(f'O maior numero da coluna 2 é: {mai}')


