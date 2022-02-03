frase = str(input('Digite uma frase: ')).strip().upper() #strip retira os espaços upper deixa maiusculo
palavras = frase.split() # split separa as frases
junto = ''.join(palavras) #.join junta tudo
inverso = junto[::-1]
print(f'a frase escrita é {frase} o inverso da frase {inverso}')
for letra in range (len(junto)-1,-1,-1):         # len de Fatiamento
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não temos um palindromo.')
