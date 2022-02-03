cont = ('Zero','Um','Dois', 'Três','Quatro','Cinco',
        'Seis','Sete','Oito','Nove','Dez',
        'Onze','Doze','Treze','Catorze','quinze',
        'Desesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:

    num = int(input('Digite um numero entre 1 e 20: '))
    if 0 <= num <= 20:
        break
    print(f'Você digitou o numero errado tente novamente.')

print(f'Você digitou o numero {cont[num]}.')
