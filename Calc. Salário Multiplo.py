#Calcula o aumento de salarío se: >R$ 1250, aumenta 10% / se menor, aumenta 15%
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))