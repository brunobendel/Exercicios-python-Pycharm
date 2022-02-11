

def aumentar(preço=0, taxa=0, formato=False):
    resp = preço+(preço*taxa/100)
    return resp if formato is False else real(resp)


def diminuir(preço=0, taxa=0, formato=False):
    resp = preço-(preço*taxa/100)
    return resp if formato is False else real(resp)


def dobro(preço=0, formato=False):
    resp = preço * 2
    return resp if formato is False else real(resp)


def metade(preço=0, formato=False):
    resp = preço / 2
    return resp if formato is False else real(resp)


def real(preço=0, moeda='R$'):
    return f'{moeda}{preço:^8.2f}'.replace('.',',')