def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

titulo('SISTEMA DE ALUNOS')
titulo('SISTEMA DE CURSOS')

def mensagem(msg):
    print('-'*30)
    print(msg)
mensagem('SISTEMA DE ALUNOS')

def soma( a,b):
    s = a + b
    print(s)
soma(4,5)

def contador (* núm): #o asterisco significa que ira receber um valor mas não se sabe quantos.
     tam = len(núm)
     print(f'Recebi os valores {núm} e são ao todo {tam} números.')
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)

