cont = ('Zero', 'Um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero=int(input('Digite um número entre 0  e 20: '))
while numero <0 or numero >20:
    print('Número inválido. ',end='')
    numero=int(input('Digite novamente: '))
print(f'Você digitou o número {cont[numero]}.')