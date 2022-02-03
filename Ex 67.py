while True:
    x = int(input('Digite a tabuada que vc deseja ver: '))
    print('~' * 30)
    if x < 0:
        break
    for c in range (1,11):
        print(f'{c} x {x} = {c*x}')
    print('~' * 30)
print('Fim')