dis = float(input('Qual a distancia da sua viagem?'))
preço = dis * 0.50 if dis <= 200 else dis *0.45
print('A sua viagem terá o valor de {:.2f} Reais'.format(preço))

# usando if simplificado tudo em uma linha.

