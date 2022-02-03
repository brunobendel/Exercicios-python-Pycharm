s= str(input('Digite seu sexo M/F:')).upper().strip()[0]
while s not in 'M/F':
    s= str(input('digite nomvamente:')).strip().upper()[0]
print(f'Sexo {s} informado com sucesso! ')