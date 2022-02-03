from time import sleep
from datetime import date
ano = int(input('Digite sua data de nascimento: '))
x = date.today().year - ano
if x < 18:
    print('Faltam {} anos pra voce se alistar'.format(18-x))
elif x == 18:
    print('Voce devera se alistar imediatamente')
elif x > 18 :
    print('Você ja passou {} anos do seu ano de alistamento'.format(x-18))

sleep(5)