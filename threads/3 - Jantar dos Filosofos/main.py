import threading


class Filosofo(threading.Thread):
    def __init__(self, nome, garfo_esquerda, garfo_direita):
        super().__init__()
        self.nome = nome
        self.garfo_esquerda = garfo_esquerda
        self.garfo_direita = garfo_direita

    def run(self):
        for _ in range(5):  # Cada filósofo medita e come 5 vezes
            self.medite()
            self.coma()

    def medite(self):
        print(f"{self.nome} está meditando.")
        # Ações de meditar

    def coma(self):
        # Tentar pegar os garfos
        with self.garfo_esquerda:
            with self.garfo_direita:
                print(f"{self.nome} está comendo.")
                # Ações de comer
        # Liberar os garfos depois de comer


if __name__ == "__main__":
    # Garfos (semáforos) compartilhados entre os filósofos
    garfos = [threading.Semaphore(1) for _ in range(5)]

    # Filósofos
    filosofos = []
    for i in range(5):
        garfo_esquerda = garfos[i]
        garfo_direita = garfos[(i + 1) % 5]
        filosofo = Filosofo(f"Filósofo {i+1}", garfo_esquerda, garfo_direita)
        filosofos.append(filosofo)

    # Iniciar as threads dos filósofos
    for filosofo in filosofos:
        filosofo.start()

    # Esperar que todas as threads terminem
    for filosofo in filosofos:
        filosofo.join()
