from random import randint
computador = randint(0,10)
print('-=-' * 20)
print('Sou seu computador, irei pensar em um número de 0 a 10, tente advinhar qual número estou pensando...')
acertou = False
while not acertou:
    jogador = int(input('Qual número eu pensei? '))
    palpites = jogador + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

print('Acertou, parabéns!. Voçê necessitou de {} tentativas.'.format(palpites))