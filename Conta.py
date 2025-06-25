import datetime
from Classes.Extrato import Extrato
#Para tornar algum dos atributos privados e encapsulados, basta colocar dois _ (__) antes do nome do atributo
#exemplo: self.__clientes = clientes

class Conta:
    __totalcontas = 0 #atributo de classe

    @classmethod
    def get_total_contas(cls):
        return cls.__totalcontas
#permite acessar o atributo de classe

    @staticmethod
    def nome_banco():
        return 'Banco do Fictício'

    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.date.today()
        self.extrato = Extrato()
        type(self).__totalcontas += 1 #permite gerar o total de contas

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(['Deposito', valor, datetime.date.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['Saque', valor, datetime.date.today()])
            return True

    def transferir(self, conta_destino, valor):
        if self.saldo < valor:
            return 'Não existe saldo suficiente na conta'
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(['Transferido', valor, datetime.date.today()])
            return 'Tranferencia realizada com sucesso'

    def gerar_saldo(self):
        print(f'Número: {self.numero}\nSaldo: {self.saldo}')