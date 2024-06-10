**Atendimento no Bar**: O funcionamento do atendimento em um bar é baseado em um bartender que recebe
o pedido dos garçons, que por sua vez recebe o pedido dos clientes. Neste contexto, o bar possui um (01)
bartender que fica esperando os garçons na copa, possui X garçons, sendo que cada garçom consegue
atender a um número limitado (C) de clientes por vez. Cada garçom somente vai para a copa para realizar
o pedido quando todos os C clientes que ele pode atender tiverem feito o pedido, ou não houver mais
clientes a serem atendidos. Um garçom deve entregar os pedidos aos seus clientes, e depois está liberado
a atender os clientes novamente. Após ter seu pedido atendido, um cliente pode fazer um novo pedido
após consumir seu pedido (o que leva um tempo aleatório). Por definição, nem todos os clientes precisam
fazer um pedido a cada rodada. Implemente uma solução que permita a passagem por parâmetro de:
a. A quantidade de clientes presentes no estabelecimento;
b. A quantidade de garçons que estão trabalhando;
c. A capacidade de atendimento dos garçons; e
d. O número de rodadas que serão liberadas no bar.
Cada garçom e cada cliente devem ser representados por threads, estruturalmente definidos como os
pseudocódigos que seguem (exemplos):