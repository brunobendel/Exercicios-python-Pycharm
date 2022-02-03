num = list()

for cont in range(0,5):
    num.append(int(input(f'Digite um valor na {cont+1}ª posição: ')))

print('-='*30)
print(f'Voce digitou os valores {num}.\nO maior foi {max(num)} e o menor foi {min(num)}')
