def contador (i, f, p):
   print(f'Contagem de {i}, até {f} de {p} em {p}')
   if i < f:
       cont = i
       while cont <= f:
           print(f'{cont} ', end='', flush=True)
           cont += p
           print('fim')
   else:
       cont = i
       while cont >= f:
           print(f'{cont} ', end='', flush=True)
           cont -= p
           print('fim')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

