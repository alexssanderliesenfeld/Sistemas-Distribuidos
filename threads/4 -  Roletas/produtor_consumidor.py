from threading import Semaphore


class ProdutorConsumidor:
    def __init__(self):
        self.conteudo = 0
        self.disponivel = False
        self.sem_produtor = Semaphore(1)
        self.sem_consumidor = Semaphore(0)

    def produzir(self, valor):
        self.sem_produtor.acquire()
        self.conteudo = valor
        self.disponivel = True
        self.sem_consumidor.release()

    def consumir(self):
        self.sem_consumidor.acquire()
        valor = self.conteudo
        self.disponivel = False
        self.sem_produtor.release()
        return valor
