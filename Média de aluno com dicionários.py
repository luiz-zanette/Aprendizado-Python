aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]} : '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Em recuperação'
else:
    aluno['media'] < 5
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é {v}')