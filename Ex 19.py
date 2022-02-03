Ex=('Desafio 19')
print('{:=^40}'.format(Ex))
from random import choice
Nm01 = input("ALUNO 01: ")
Nm02 = input("ALUNO 02: ")
Nm03 = input("ALUNO 03: ")
Nm04 = input("ALUNO 04: ")
Lista = [Nm01, Nm02, Nm03, Nm04]
Sort = choice(Lista)
print('Aluno sorteado: {}'.format(Sort))
