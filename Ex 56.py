somaidade = 0
mulher20 = 0

for p in range(1,5):
     print(f'------{p}º Pessoa -------')
     nome = str(input('Nome:'))
     idade = int(input('Idade: '))
     sexo = str(input('Sexo M/F: ')).strip()
     somaidade += idade
     if p == 1 and sexo in 'Mm':
         maioridadehomem = idade
         nomevelho = nome
     if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
     if sexo in 'fF'and idade < 20:
         mulher20 += 1


médiaidade= somaidade/ 4
print(f'A média da idade é {médiaidade}\nO nome do homem mais velho é {nomevelho} e maior idade do homem é {maioridadehomem}\ne tem {mulher20} com menos de 20 anos')
