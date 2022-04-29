
#Tipos primitivos De input

a = input('Digite algo:')
print('O tipo primitivo de valor é', type(a))
print('só tem espaços?', a.isspace())
print('Esse é um numero?', a.isnumeric())
print("Esse é alfabetico? ", a.isalpha())
print("Esse é alfanumerico?",a.isalnum())
print("Está em maiusculas?",a.isupper())
print("Está em minusculas?", a.islower())
print('Está captalizada?', a.istitle()) #quando tem letras maiuscyulas e minusculas.

num = [6, 2, 1, 4, 3]
print(num.sort())