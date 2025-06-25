def área (larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg} x {comp} é de {a}m2')


print('Controle de Terrenos')
print('=-'*30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
área (larg, comp)