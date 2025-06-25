frase = 'Curso em Python'
print(frase)
print(frase[3])
print(frase[4:15])
print(frase[5:])
print(frase[:10])
print(frase[2:15:3])
print(frase[1::2])
print(frase[::4])
print(frase[4::])
print("""Aqui pode ser inserido um texto longo
com grande com grande numero de linhas e frases,
desde que coloque
tanto ao inicio quanto ao final tres 'aspas'""")

frase2 = '   Aprenda Python  '
print(frase2.count('p'))
print(frase2.upper()).count('P')
print(frase2.upper())
print(frase2.lower())
print(len(frase2))
print(fras2.strip())
print(frase2.lstrip())
print(frase2.rstrip())
print(frase2.replace('Python', 'Android')) #troca neste momento a palavra, mas não salva a mudança.
frase2 = frase2.replace('Python', 'Android')#mantêm salvo a mudança
print('Curso' in frase2)
print( frase2.find('Phyton'))

frase3 = 'Curso em Video Python'
print(frase3.split())
print('-'.join(frase3))
divido = frase3.split()
print(divido[0])
print(divido[2][3])
