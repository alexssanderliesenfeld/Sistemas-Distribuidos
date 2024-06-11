from roleta import Roleta
from conta_bancaria import ContaBancaria
from produtor_consumidor import ProdutorConsumidor
import threading
import time


def teste_roleta():
    roleta = Roleta()
    print("Número sorteado:", roleta.girar())


def teste_conta_bancaria():
    conta1 = ContaBancaria(1000)
    conta2 = ContaBancaria(2000)

    conta1.depositar(500)
    conta1.sacar(200)
    conta1.creditar_juros(0.05)
    conta1.transferir(conta2, 300)

    print("Saldo conta1:", conta1.get_saldo())
    print("Saldo conta2:", conta2.get_saldo())


def teste_produtor_consumidor():
    buffer = ProdutorConsumidor()

    def produtor():
        for i in range(5):
            try:
                buffer.produzir(i)
                print("Produziu:", i)
                time.sleep(0.5)
            except Exception as e:
                print(e)

    def consumidor():
        for i in range(5):
            try:
                valor = buffer.consumir()
                print("Consumiu:", valor)
                time.sleep(0.5)
            except Exception as e:
                print(e)

    prod_thread = threading.Thread(target=produtor)
    cons_thread = threading.Thread(target=consumidor)

    prod_thread.start()
    cons_thread.start()

    prod_thread.join()
    cons_thread.join()


if __name__ == "__main__":
    print("Teste da Roleta:")
    teste_roleta()

    print("\nTeste da Conta Bancária:")
    teste_conta_bancaria()

    print("\nTeste do Produtor-Consumidor:")
    teste_produtor_consumidor()
