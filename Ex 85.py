valor = 0
num = [[],[]]

for c in range (0,7):
    valor = int(input(f'Digite o {c+1}° valor:'))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
print(f'Os numeros pares foram {num[0]}\nOs numeros ímpares foram {num[1]}.')



