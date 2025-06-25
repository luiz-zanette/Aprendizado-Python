lista = ('Casa', 'Vaga', 'Hotel', 'Programar', 'Computador', 'Python')
for c in lista:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end='') #primeiro upper para deixar tudo maiusculo
    for letra in c:
        if letra.lower() in 'aeiou': #jogar em lower para pegar mesmo com a letra maiuscula
            print(letra, end=' ')