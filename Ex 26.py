fr =str(input('digite uma frase: ')).upper().strip()
print('Sua frase contem {} vezes a Letra A'.format(fr.count('A')))
print('A primeira vez q aparece a letra "a" é na posição {}'.format(fr.find('A')+1))
print('A ultima letra "A" apreceu na {} posição '.format(fr.rfind('A')+1))
