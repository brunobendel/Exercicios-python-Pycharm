Ex=('Desafio 20')
print('{:=^50}'.format(Ex))
import random
Nm01 = input("ALUNO 01: ")
Nm02 = input("ALUNO 02: ")
Nm03 = input("ALUNO 03: ")
Nm04 = input("ALUNO 04: ")
lista = [Nm01, Nm02, Nm03, Nm04]
random.shuffle(lista)
print('Aluno sorteado: {}'.format(lista))
