numero=int(input('Digite um número e eu direi se ele é par ou ímpar: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é impar'.format(numero))