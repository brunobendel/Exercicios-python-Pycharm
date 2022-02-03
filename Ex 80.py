lista = []

for c in range(0,5):
    num = int(input('Digite um numero na lista: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Valor inserido no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num) #quando usado insert(posição , Valor inserido)
                print(f'Valor inserido na posição {pos} da lista')
                break
            pos += 1

print(f'Os valores digitados na lista em ordem foram {lista}.')
