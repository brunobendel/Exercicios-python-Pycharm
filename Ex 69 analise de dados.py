ex = 'Cadastro de pessoas:'
print(f'{ex:=^40}')
pessoas = 0
totalhomens = 0
mulhercommenosdevinte = 0
while True:
    print('~=' * 20)
    Idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o Sexo M/F: ')).upper().strip()[0]
    print('~=' * 20)
    Cont = str(input('Deseja continuar? ')).upper().strip()[0]
    if Idade > 18:
        pessoas += 1
    if sexo in 'M':
        totalhomens += 1
    if sexo in 'F' and Idade < 20:
        mulhercommenosdevinte += 1

    if Cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {pessoas}\nAo todo temos {totalhomens} Homens cadastrados\nE temos {mulhercommenosdevinte} mulheres com menos de 20 ano.')



