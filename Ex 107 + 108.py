
from uteis import  moedas
#Programa principal
p = float(input('Digite qual valor você usará no modulo moedas: R$'))
print(f'O valor {moedas.real(p)} mais 10% é {moedas.real(moedas.aumentar(p,10))}')
print(f'O valor {moedas.real(p)} menos 20% é {moedas.real(moedas.diminuir(p,20))}')
print(f'O valor é {moedas.real(p)} e o dobro é {moedas.real(moedas.dobro(p))} ')
print(f'O valor {moedas.real(p)} e a metade é {moedas.real(moedas.metade(p))}')
