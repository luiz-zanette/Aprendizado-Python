valor = []
maior = menor = 0
for c in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        if valor[c] < menor:
            menor = valor[c]
print(f'Voce digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}...', end='')

