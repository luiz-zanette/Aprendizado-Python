def escreva (msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

print(escreva('Luiz Henrique - linhas autoajustadas'))
print(escreva('Curso de Python no Youtube'))
print(escreva('CeV'))