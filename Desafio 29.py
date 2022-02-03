v = int(input('Digite a velocidade do seu carro: '))
if v<= 80:
    print('\033[7mParabens você está dentro da velocidade permitida.')
else:
    m = v-80
    i = m * 7
    print('\033[31mVocê vai receber uma multa no valor de R${}'.format(i))

#30 branco       \033[0;33;44m  na primeira  0= none 1=bold 4=underline 7=negative
#31 vermelho
#32 verde
#33 amarelo
#34 azul
#35 roxo
#36 outro azul
#37 cinza