n = str(input('Digite um nome: ')).strip() #retira os espaços do inicio e fim
n = n.split() #separa as frases pelos espaços
print('seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é: {}'.format(n[len(n)-1]))
#len vem de length=comprimento que mostra o comprimento da frase em caractere.
