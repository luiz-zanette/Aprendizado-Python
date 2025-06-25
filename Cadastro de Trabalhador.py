import datetime
cadastro = {}
cadastro['Nome'] = str(input('Digite o nome do funcionário: '))
nascimento = int(input('Digite o ano de nascimento: '))
cadastro['Idade'] = datetime.date.today().year - nascimento
cadastro['CTPS'] = int(input('Digite a CTPS (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['ano contrato'] = int(input('Digite o ano de contratração: '))
    cadastro['salário'] = (float(input(f'Digite o salário: R$ ')))
    cadastro['aposentadoria'] = cadastro['Idade'] + ((cadastro['ano contrato'] + 35) - datetime.date.today().year)

print('-=' * 30)
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')