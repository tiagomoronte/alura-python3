class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O Saldo do titular {} é {}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)




conta1 = Conta(123, "Joao", 100.00, 1000.0)
conta2 = Conta(123, "Joao", 100.00, 1000.0)
conta1.extrato()
conta2.extrato()
conta1.transferir(10, conta2)
conta1.extrato()
conta2.extrato()
