frase = input('Digite uma frase: ').strip()
print('Sua frase em caixa alta fica: {}.'.format(frase.upper()))
print('Sua frase em minúscula fica: {}.'.format(frase.lower()))
print('Sua frase tem ao todo {} letras.'.format(len(frase) - frase.count(' ')))

