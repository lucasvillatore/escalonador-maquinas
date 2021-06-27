def splita_entrada_em_inteiros(entrada):
    quantidade_x, quantidade_y = entrada.split(' ')

    quantidade_x = int(quantidade_x)
    quantidade_y = int(quantidade_y)


    return quantidade_x, quantidade_y

def descobre_valor_soma_total(equacao_total):
    soma = 0
    for i in range(0, len(equacao_total)):
        soma += equacao_total[i]['tempo_em_minutos']
    return soma
    
def descobre_equacoes(pedidos, equacao_atual = [], indice = 0, limiar = 0, menor_pedido = []):
    global equacao_resposta

    soma_total = descobre_valor_soma_total(equacao_atual)
    if (indice >= len(pedidos)):
        if (limiar - soma_total < menor_pedido['tempo_em_minutos']):
            equacao_resposta.append(equacao_atual)
        return

    descobre_equacoes(pedidos, equacao_atual.copy(), indice + 1, limiar, menor_pedido)

    if (pedidos[indice]['tempo_em_minutos'] + soma_total <= limiar):
        equacao_atual.append(pedidos[indice])
        descobre_equacoes(pedidos, equacao_atual.copy(), indice, limiar, menor_pedido)


def descobre_menor_pedido(pedidos):
    menor = pedidos[0]

    for i in range(0, len(pedidos)):
        if (pedidos[i]['tempo_em_minutos']):
            menor = pedidos[i]

    return menor

equacao_resposta = []
if __name__ == "__main__":
    tempo_maximo_dia = 300
    # quantidade_maquinas_quantidade_pedidos = input()
    # quantidade_maquinas, quantidade_pedidos = splita_entrada_em_inteiros(quantidade_maquinas_quantidade_pedidos)

    # pedidos = []

    # for i in range(0, quantidade_pedidos):
    #     quantidade_utilizacao_quantidade_minutos = input()
    #     quantidade_utilizacao, quantidade_minutos = splita_entrada_em_inteiros(quantidade_utilizacao_quantidade_minutos)

    #     pedido = {
    #         'quantidade': quantidade_utilizacao,
    #         'tempo_em_minutos': quantidade_minutos
    #     }
    #     pedidos.append(pedido)
    pedidos = [{'quantidade': 97, 'tempo_em_minutos': 135}, {'quantidade': 610, 'tempo_em_minutos': 108}, {'quantidade': 395, 'tempo_em_minutos': 93}, {'quantidade': 211, 'tempo_em_minutos': 42}]

    pedidos = sorted(pedidos, key=lambda k: k['tempo_em_minutos'], reverse=True) 
    
    menor_pedido = descobre_menor_pedido(pedidos)
    descobre_equacoes(pedidos, [], 0, tempo_maximo_dia, menor_pedido)








