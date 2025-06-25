nome = str(input('Insira seu nome: '))
if nome == 'Luiz':
    print('Que nome bonito!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a seugunda nota: '))
m = (n1 + n2) / 2
print('Sua média é: {:.1f}' .format(m))

if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média precisa melhorar, estude mais')