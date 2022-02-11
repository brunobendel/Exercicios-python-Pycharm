
from uteis import  moedas
#Programa principal
p = float(input('Digite qual valor você usará no modulo moedas: R$'))
print('~'*50)
print('VALORES'.center(50))
print('~'*50)
print(f'O valor {moedas.real(p)} mais 10% é \t{moedas.aumentar(p,10,True)}')
print(f'O valor {moedas.real(p)} menos 20% é \t{moedas.diminuir(p,20,True)}')
print(f'O valor {moedas.real(p)} o dobro é \t{moedas.dobro(p,True)} ')
print(f'O valor {moedas.real(p)} a metade é \t{moedas.metade(p,True)}')
print('~'*50)