time = ('Sport', 'Cruzeiro', 'Palmeiras', 'São Paulo', 'Flamengo', 'Bahia', 'Santos', 'Vasco')
print(f'Lista dos times da lista {time}')
print(f'Os cincos primeiros colocados são {time[0:5]}')
print(f'Os quatro últimos colocados são {time[-4:]}')
print(f'Times em ordem alfabética {sorted(time)}')
print(f'O São Paulo está na {time.index('São Paulo')+1} posição')
