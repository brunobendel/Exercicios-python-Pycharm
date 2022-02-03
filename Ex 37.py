from time import sleep
n = int(input('Digite um numero:'))
print('''Escolha uma base para conversão:
[1] Converte para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Digite sua opção: '))

if opção == 1:
    print('Seu numero em Binario é: {}'.format(bin(n)[2:]))
elif opção == 2:
    print('Seu numero em Octal é: {}'.format(oct(n)[2:]))
elif opção == 3:
    print('Seu numero em Hexadecimal é: {}'.format(hex(n)[2:]))
else:
    print('Opção invalida')

sleep(3)