casa = float(input('Digite o calor da casa: '))
salario = float(input('Digite o valor do seu salario: '))
anos = int(input('Digite em quantos anos vc quer pagar essa casa: '))
mensal = casa/(anos*12)
print('Para pagar uma casa de R${:.2f}\nVocê vai precisar pagar por mes R${:.2f}\nE 30% do seu salario é R${:.2f}'.format(casa,casa/(anos*12),salario*0.3))
if salario * 0.3 >= mensal:
    print('Parabens seu emprestimo foi aprovado')
else:
    print('Seu imprestimo foi negado.')
