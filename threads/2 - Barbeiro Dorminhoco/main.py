import random
import threading
import time

class BarbeiroDorminhoco:
    def __init__(self, cadeiras):
        self.cadeiras = cadeiras
        self.clientes_esperando = 0  # Número de clientes esperando
        self.mutex = threading.Lock()  # Mutex para proteger as variáveis compartilhadas
        self.barbeiro_dormindo = True  # Sinalizador para indicar se o barbeiro está dormindo
        self.barbeiro_monitor = threading.Condition(self.mutex)  # Monitor para o barbeiro

    def cortar_cabelo(self, cliente):
        with self.mutex:
            self.clientes_esperando -= 1
            print(f"{cliente.nome} está cortando o cabelo.")
            time.sleep(3)  # Simula o tempo de corte de cabelo
            print(f"{cliente.nome} terminou o corte de cabelo.")

    def atender_cliente(self):
        with self.mutex:
            if self.barbeiro_dormindo:
                self.barbeiro_dormindo = False
                self.barbeiro_monitor.notify()  # Acorda o barbeiro
            self.clientes_esperando += 1
            print(f"{cliente.nome} está esperando por uma cadeira.")

    def esperar_cadeira(self):
        with self.mutex:
            while self.clientes_esperando >= self.cadeiras or self.barbeiro_dormindo:
                self.barbeiro_monitor.wait()  # Espera o barbeiro estar disponível
            print(f"{cliente.nome} sentou-se na cadeira.")

class Cliente(threading.Thread):
    def __init__(self, nome, barbeiro):
        super().__init__()
        self.nome = nome
        self.barbeiro = barbeiro

    def run(self):
        self.barbeiro.atender_cliente()
        self.barbeiro.esperar_cadeira()
        self.barbeiro.cortar_cabelo(self)

barbeiro = BarbeiroDorminhoco(3)  # 3 cadeiras na barbearia
num_clientes = 5  # Número de clientes

clientes = []
for i in range(num_clientes):
    cliente = Cliente(f"Cliente {i+1}", barbeiro)
    clientes.append(cliente)

for cliente in clientes:
    cliente.start()

time.sleep(10)  # Tempo de simulação

barbeiro.barbeiro_monitor.acquire()
barbeiro.barbeiro_dormindo = True
barbeiro.barbeiro_monitor.notify()
barbeiro.barbeiro_monitor.release()
