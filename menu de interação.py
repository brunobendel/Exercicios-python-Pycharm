Primeiro = int(input('Digite o primeiro valor: '))
Segundo = int(input('Digite o Segundo valor: '))
x = int(input('Escolha sua Opção\n[1] soma\n[2] multiplicação\n[3] maior\n[4] novos numeros\n[5] sair\nQual a sua opção? '))

while x != 5:
    if x == 1:
        print(f'A soma é \033[031m{Primeiro+Segundo}')
        x = int(input('\033[0mEscolha sua Opção\n[1] soma\n[2] multiplicação\n[3] maior\n[4] novos numeros\n[5] sair\nQual a sua opção? '))

    elif x == 2:
        print(f'A soma é \033[031m{Primeiro * Segundo}')
        x = int(input('\033[0mEscolha sua Opção\n[1] soma\n[2] multiplicação\n[3] maior\n[4] novos numeros\n[5] sair\nQual a sua opção? '))

    elif x == 3:
        if Primeiro > Segundo:
            print(f'A soma é \033[031m{Primeiro}')
            x = int(input('\033[0mEscolha sua Opção\n[1] soma\n[2] multiplicação\n[3] maior\n[4] novos numeros\n[5] sair\nQual a sua opção? '))
        else:
            print(f'A soma é \033[031m{Segundo}')
            x = int(input('\033[0mEscolha sua Opção\n[1] soma\n[2] multiplicação\n[3] maior\n[4] novos numeros\n[5] sair\nQual a sua opção? '))
    elif x == 4:
        Primeiro = int(input('Digite o primeiro valor: '))
        Segundo = int(input('Digite o Segundo valor: '))
        x = int(input('\033[0mEscolha sua Opção\n[1] soma\n[2] multiplicação\n[3] maior\n[4] novos numeros\n[5] sair\nQual a sua opção? '))
    else:
        print('opção invalida tente novamente.')
        x = int(input('\033[0mEscolha sua Opção\n[1] soma\n[2] multiplicação\n[3] maior\n[4] novos numeros\n[5] sair\nQual a sua opção? '))

