
def contador(i=0,f=0,p=1):
    """
    Contador feito Pelo Bruno na aula do guanabara:
    :param i: parametro inicial
    :param f: parametro final
    :param p: Passo
    :return: printa os valores do inicio ao fim contando pelo passo.
    """
    c = i
    while c<=f:
        print(f'{c}', end=" ")
        c += p
    print('Fim!')

contador(0,10,2)
help(contador)
