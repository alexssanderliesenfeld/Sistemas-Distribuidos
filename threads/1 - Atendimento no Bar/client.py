from asyncio import sleep

def fazer_pedido():
    pass

def receber_pedido():
    pass

def consome_pedido():
    pass

def cliente():
    maximo_rodada = 20
    round = 0
    print('cliente chegou')
    while(maximo_rodada<round):
        fazer_pedido()
        sleep(1)
        receber_pedido()
        consome_pedido()
        round+=1
    print('cliente for dormir')
