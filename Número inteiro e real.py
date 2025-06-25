def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Valor digitado inválido, tente novamente.')
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Valor digitado inválido, tente novamente.')
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')