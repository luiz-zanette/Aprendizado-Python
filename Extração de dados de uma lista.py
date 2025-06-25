valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r not in 'SsNn':
        print('ERRO! Digite apenas S ou N.')
    if r in 'Nn':
        break
print(f'Você digitou {len(valor)} elementos.')
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

