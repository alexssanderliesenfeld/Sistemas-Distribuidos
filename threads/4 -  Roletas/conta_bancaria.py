class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def creditar_juros(self, taxa):
        self.saldo *= (1 + taxa)

    def transferir(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.depositar(valor)
        else:
            print("Saldo insuficiente para transferência.")

    def get_saldo(self):
        return self.saldo
