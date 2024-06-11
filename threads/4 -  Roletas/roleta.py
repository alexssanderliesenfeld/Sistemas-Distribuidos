import random


class Roleta:
    def __init__(self):
        self.numero = 0

    def girar(self):
        self.numero = random.randint(0, 36)
        return self.numero
