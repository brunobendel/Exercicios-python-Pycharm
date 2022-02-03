temp = []
princ = []
maior = menor = 0
while True:

    temp.append(str(input('Digite um nome:')))
    temp.append(float(input('Digite o Peso:')))
    if len(princ) == 0:
        menor = maior = temp[1]
    else:
        if temp [1] > maior:
            maior = temp [1]
        if temp [1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar: [S/N]'))

    if resp in 'Nn':
        break
print(f'No total foram {len(princ)} pessoas cadastradas.')
print(f'A pessoa mais pesada tem {maior} Kg ',end='')

for p in princ:
    if p[1] == maior:
        print(f' {p[0]}',end='')
print(f'A pessoa mais leve tem {menor} ', end='')
for p in princ:
    if p[1] == menor:
        print(f' {p[0]}', end='')

