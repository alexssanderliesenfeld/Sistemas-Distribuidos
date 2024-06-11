import threading 
from client import cliente
from garcon import garcon

numero_de_pedidos_por_garcon = 2

pedidos = []
garcons = []
clientes = []

def fazer_pedido(pedido):
    print('feito pedido')
    pedidos.append(pedido)
    return len(pedidos)

def bar_tender():
    print('bar aberto')
    for i in range(5):
        print(f'adicionado cliente {i}')
        cl = threading.Thread(target=cliente)
        cl.run()
    print('\n')
    for i in range(5):
        print(f'adicionado garçon {i}')
        garcons.append(threading.Thread(target=garcon, args=[clientes]))
        # garcons[i].run()

if __name__ == '__main__':
    bar_tender()
# threading.Thread(target=)