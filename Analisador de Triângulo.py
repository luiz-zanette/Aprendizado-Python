#Analisa o comprimento de 3 segmentos e verifica se elas podem formar um triângulo
print('=-=' *25)
print('Analisador de trinângulos')
print('=-=' *25)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO!')

