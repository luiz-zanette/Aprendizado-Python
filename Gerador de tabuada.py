#Lê um número inteiro e exibe sua tabuada
print('Irei exibir a tabuada do número desejado')
tab = int(input('Insira um número para exibir sua tabuada:'))
for c in range(1, 11):
    print('{} x {} = {}' .format(tab, c, tab*c))