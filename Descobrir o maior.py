from time import sleep
def maior(* núm):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
         if valor > maior:
            maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo'
          f'\nO maior valor informado foi {maior}')


#PP
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)