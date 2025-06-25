#Lê a velocidade do carro, se ultrapassar 80km/h, calcula a multa em R$7,00 por km excedido
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade <=80:
    print('Você está dentro do limite permitido, parabéns, diriga em segurança')
else:
    print('Você ultrapassou os 80km permitidos')
    multa = (velocidade - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
    print('Reduza e diriga com segurança!')