
from uteis import  moedas
#Programa principal
p = float(input('Digite qual valor você usará no modulo moedas: R$'))
print(f'O valor {moedas.real(p)} mais 10% é {moedas.aumentar(p,10,True)}')
print(f'O valor {moedas.real(p)} menos 20% é {moedas.diminuir(p,20,True)}')
print(f'O valor é {moedas.real(p)} e o dobro é {moedas.dobro(p,True)} ')
print(f'O valor {moedas.real(p)} e a metade é {moedas.metade(p,True)}')
