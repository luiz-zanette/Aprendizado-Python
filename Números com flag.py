soma = cont = 0
while True:
    num = int(input('Digite um valor: (digite 999 para parar) '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos valores foi {soma}')
print(f'O total de numeros digitados foram de {cont}')

