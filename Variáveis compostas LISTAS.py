num = [2,5,4,9,10,3]
print(num)
num[2] = 3 #altera o valor do item 2 para 3
print (num)
num.append(7) #adiciona um item ao final da lista
print(num)
num.insert(2, 0)    #insere o valor 0 na posição de elemento 2 e reorganiza a lista
print(num)
num.sort() # organiza a lista em ordem crescente
print(num)
num.sort(reverse=True) #organiza a lista em ordem decrescente
print(num)
print(f'Essa lista tem {len(num)} elementos') #mostra quantos elementos tem na lista
num.pop() #remove o último elemento da lista
print(num)
num.remove(5) #remove o elemento 5 da lista
print(num)
if 5 in num:
    num.remove(5)
else:
    print('Não acheio o número 5') #tenta remover o numero digitado na lista e se não encontrar, mostra essa mensagem

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!') #apresenta a posição e o valor que está adotado

for cont in range (0,5):
    num.append(int(input('Digite um valor: '))) #Apresenta os valores inseridos
