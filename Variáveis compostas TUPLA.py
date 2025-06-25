lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(len(lanche))
for cont in range (0, len(lanche)):
    print(lanche[cont])
print(sorted(lanche))