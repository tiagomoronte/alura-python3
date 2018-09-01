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

    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limiete".format(valor))


    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {"BB": "00'", "Caixa": "104"}


conta1 = Conta(123, "Joao", 100.00, 1000.0)
conta2 = Conta(123, "Joao", 100.00, 1000.0)
conta1.extrato()
conta2.extrato()
conta1.transferir(10, conta2)
conta1.extrato()
conta2.extrato()


conta2.sacar(100000.00)
print(Conta.codigos_bancos())