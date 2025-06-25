#OPERADORES ARITMÉTICOS
n1 = int(input('Insira um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 # divisão inteira
p = n1 ** n2 #potência
rd = n1 % n2 #resto divisão

print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s,m,d))
print('A divisão inteira vale {}, a potência vale {}, o resto da divisão vale {}'.format(di,p,rd))

print('=' * 5, 'Nova linha estética', '=' * 5)
print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}. '.format(s,m,d), end='') #end une as linhas, pode escrever algo
print('A divisão inteira vale {}. \n A potência vale {}. \n O resto da divisão vale {}'.format(di,p,rd)) #\n quebra a linha

print(n1 * 20)
print('=' * 5, n2, '=' * 5)

#OPERADOR ALFANUMÉRICO
nome = input('\nInsira seu nome:')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:15}!'.format(nome))
print('Prazer em te conhecer {:>15}!'.format(nome))