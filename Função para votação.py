def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade > 16 and idade <18 or idade > 65:
      return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        idade > 18
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


#Programa Principal
nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))