num = (int(input('Digite um numero:')),
int(input('Digite um numero:')),
int(input('Digite um numero:')),
int(input('Digite um numero:')))

print(f'Você digitou os valores: {num}')
print(f'O Valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 Apareceu na {num.index(3)+1}ª Posição. ')
else:
    print('Não foi digitado nenhum numero 3')
print(f'Foram digitados numeros pares sendo eles' ,end=' ')
for n in num: # Para cada n em num(tupla) verifique se é par.
    if n % 2 == 0:
        cont += 1
        print(n, end=' ')
