nome = 'Luiz'
nome =str(input('Qual é o seu nome? '))
if nome == 'Luiz':
    print('Que nome bonito!')
    print('Bom dia, {}!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
    print('Bom dia, {}!'.format(nome))
else:
   print('Seu nome é bem normal')
   print('Bom dia, {}!'.format(nome))