from asyncio import sleep


def cliente():
    max_rodada = 20
    round = 0
    print('cliente chegou')
    while(max_rodada<round):
        # fazer_pedido()
        sleep(1)
        #   receber_pedido()
        #   consome_pedido()
        round+=1
        pass
    print('cliente for dormir')
