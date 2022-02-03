soma = cont = 0
while True:
    num = int(input('Digite um valor ou digite 999 para parar: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Esse numero foi escrito {cont} vezes e a soma é {soma}.')