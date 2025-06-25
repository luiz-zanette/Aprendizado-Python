#Calcula o preço da passagem cobrando R$ 0,50/km para viagens até 200km e R$ 0,45 para mais longas.
from time import sleep
distancia = float(input('Qual a distância da sua viagem? '))
print('Você está iniciando uma viagem de {:.0f} KM' .format(distancia))
print('PROCESSANDO...')
sleep(2)

if distancia <= 200:
    preco = distancia * 0.50
    print('O custo da sua viagem é: R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O custo da sua viagem é R${:.2f}'.format(preco))

print('BOA VIAGEM!')


