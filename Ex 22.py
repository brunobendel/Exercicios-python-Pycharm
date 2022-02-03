nome = str(input("Digite seu nome inteiro: ")).strip()
print('Analizando seu nome....')
print('Seu nome em Maiusculas: {}'.format(nome.upper()))
print('Seu nome em minusculas: {}'.format(nome.lower()))
print('Seu nome tem quantas letras retirando os espaços: {}'.format(len(nome)- nome.count(' ')))  #len conta quantos caracteres tem na str e count conta os espaços
print('Seu nome tem {} letras '.format(nome.find(' ')))
separa = nome.split() #split quebra as palavras entre os espaços.
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0],len(separa[0])))