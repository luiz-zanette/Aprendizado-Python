#Modo colchetes
nome = 'Luiz'
print('Prazer em te conhecer: {} {} {}' .format('\033[1;33;40m', nome, '\033[m\n'))

#Modo na frase
print('\033[1;33m Olá mundo, \033[7;36;40m como vai?\033[m')

#Modo Dicionário
nome = 'Luiz'
sobrenome = 'Henrique'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('\nPrazer em te conhecer: {} {} {} {}'.format(cores['azul'], nome, cores['amarelo'], sobrenome))