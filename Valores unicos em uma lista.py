valor = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')

    r = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if r not in 'SsNn':
        print('ERRO! Digite apenas S ou N.')
        r = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if r in 'Nn':
        break

valor.sort()
print(f'Você digitou os valores {valor}')
