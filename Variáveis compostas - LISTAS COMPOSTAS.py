teste = list ()
teste.append('Gustavo')
teste.append((36))
galera=list()
galera.append(teste[:])
teste[0] = 'Maria'
teste [1] = 22
galera.append(teste[:])
print(galera)


lista = [['João', 19], ['Ana', 33], ['Carlos', 13], ['Joaquim', 12]]
print(lista[0][0])
print(lista[2][1])
print('='*15)
for p in lista:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
