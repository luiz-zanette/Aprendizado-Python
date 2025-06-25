from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Classes.Contaespecial import Contaespecial

#Teste do código
cliente1 = Cliente('João', '123123123', 'Rua quadrada')
cliente2 = Cliente('Maria', '456456456', 'Rua redonda')
cliente3 = Cliente('Pedro', '789789789', 'Rua peculiar')

conta1 = Conta([cliente1,cliente2], 110, 0)
conta3 = Contaespecial([cliente3], 120, 2000, 500)

#conta1.depositar(1000)
#conta1.sacar(200)
#conta1.extrato.gerar_extrato(conta1.numero)


#print(f'Cliente 1: {cliente1.nome, cliente1.rua}')
#print(f'Cliente 2: {cliente2.nome, cliente2.rua}')
#print(f'Até agora temos {Conta.get_total_contas()} contas cadastradas')
#print(f'Bem vindo ao {Conta.nome_banco()}')

conta3.depositar(800)
conta3.sacar(300)
conta3.extrato.gerar_extrato(conta3.saldo)
