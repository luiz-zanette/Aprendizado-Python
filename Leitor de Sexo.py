sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, digite novamente')).strip().upper()[0]
sprint ('Sexo {} registrado com sucesso'.format(sexo))
