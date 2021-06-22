

def splita_entrada_em_inteiros(entrada):
    quantidade_x, quantidade_y = entrada.split(' ')

    quantidade_x = int(quantidade_x)
    quantidade_y = int(quantidade_y)

    return quantidade_x, quantidade_y


if __name__ == "__main__":

    quantidade_maquinas_quantidade_pedidos = input()
    quantidade_maquinas, quantidade_pedidos = splita_entrada_em_inteiros(quantidade_maquinas_quantidade_pedidos)

    pedidos = []

    for i in range(0, quantidade_pedidos):
        quantidade_utilizacao_quantidade_minutos = input()
        quantidade_utilizacao, quantidade_minutos = splita_entrada_em_inteiros(quantidade_utilizacao_quantidade_minutos)

        pedido = {
            'quantidade': quantidade_utilizacao,
            'tempo_em_minutos': quantidade_minutos
        }
        pedidos.append(pedido)

    print(pedidos)