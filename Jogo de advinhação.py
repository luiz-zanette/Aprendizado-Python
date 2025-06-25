from random import randint
from time import sleep
computador = randint(0,5) #Computador sorteia o número
print('===' * 25)
print('Vamos jogar, vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('===' * 25)
jogador = int(input('Em qual número pensei?:')) #Jogador tenta advinhar
print('Processando...')
sleep(1)
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Você errou! Eu pensei no número {} e não no {}.'.format(computador, jogador))


