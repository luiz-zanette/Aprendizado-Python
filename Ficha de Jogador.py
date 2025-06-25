def ficha (jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

#Programa Principal
nome = str(input('Nome do jogador: '))
qtdgols = str(input('Quantidade de gols: '))

if qtdgols.isnumeric():
    qtdgols = int(qtdgols)
else:
    qtdgols = 0

if nome.strip() == '':
    ficha(gols=qtdgols)
else:
    ficha(nome, qtdgols)