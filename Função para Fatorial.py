def fatorial(n, show=False):
    """
    :param n: O número a ser calculado
    :param show: (opcional), mostra a conta
    :return: retorna o valor fatorial do numero n.
    """

    f = 1 #determina o valor inicial do fatorial
    for c in range(n, 0, -1): #explica que desejo começar do valor n, até 0, voltando 1 casa.
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#Programa Principal
print(fatorial(5, show=True))
help(fatorial)