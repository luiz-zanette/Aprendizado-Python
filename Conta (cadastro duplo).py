#Codigo da classe
class Conta:                                             #Inicialização da classe
    def __init__(self, numero, cpf, titular, saldo):          # Construtor da classe
        self.numero = numero
        self.cpf = cpf
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print(f'Número da conta: {self.numero}')
        print(f'CPF do titular: {self.cpf}')
        print(f'Titular da conta: {self.titular}')
        print(f'Saldo da conta: {self.saldo}')

    def transferir(self, contadestino, valor):
        if self.saldo < valor:
            return ('Não existe saldo suficiente')
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            print('Transferencia realizada com sucesso')

#Código de exemplo
conta1 = Conta (123, 996234, 'Maria', 0)
conta2 = Conta (222, 123456789, 'João', 500)

if conta1 == conta2:
    print('São iguais')
else:
    print('São diferentes')

conta2.transferir(conta1, 100)
print('='*30)
print('Conta de origem')
conta1.extrato()
print('='*30)
print('Conta de destino')
conta2.extrato()