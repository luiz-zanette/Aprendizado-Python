tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'Mm':
        totH =+ 1
    if sexo == 'Ff' and idade < 20:
        totM20 =+ 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Há {tot18} pessoas com mais de 18 anos')
print(f'Foram cadastradas {totH} homens')
print(f'Há {totM20} mulheres com menos de 20 anos')
