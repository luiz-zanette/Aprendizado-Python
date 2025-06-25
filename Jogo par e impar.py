from random import randint
vitoria = 0
print('==='*10)
print('Jogo do par ou impar')
print('==='*10)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Você digitou {jogador} e o computador {computador}. Total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu')
            vitoria += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
            vitoria += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {vitoria} vezes.')

