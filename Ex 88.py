aluno = []

while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    média = (nota1 + nota2)/2
    resp = str(input('Deseja continuar (S/N) : '))
    aluno.append([nome,[nota1,nota2],média])

    if resp in 'Nn':
        break
print(f'{"N°.":<6}{"Nome":<8}{"Média":>10}')
print('-=' * 20)
for d, n in enumerate(aluno):
    print(f'{d:<6} {n[0]:<8}{n[2]:>10.1f}')
print('--' * 20)
while True:

    notas = int(input('Você deseja mostrar a nota de algum aluno? Sair 999:\n'))

    if notas == 999:
        break

    if notas<= len(aluno)-1:
        print(f' O Aluno:{aluno[notas][0]}, Tirou {aluno[notas][1]} ')






