#!/usr/bin/python3

def splita_entrada_em_inteiros(entrada):
    quantidade_x, quantidade_y = entrada.split()

    quantidade_x = int(quantidade_x)
    quantidade_y = int(quantidade_y)


    return quantidade_x, quantidade_y

def descobre_valor_soma_total(equacao_total):
    soma = 0
    for i in range(0, len(equacao_total)):
        soma += equacao_total[i]['tempo_em_minutos']
    return soma
    
def descobre_variaveis(pedidos, equacao_atual = [], indice = 0, limiar = 0, menor_pedido = []):
    global variaveis

    soma_total = descobre_valor_soma_total(equacao_atual)
    if (indice >= len(pedidos)):
        if (limiar - soma_total < menor_pedido['tempo_em_minutos']):
            variaveis.append(equacao_atual)
        return

    descobre_variaveis(pedidos, equacao_atual.copy(), indice + 1, limiar, menor_pedido)

    if (pedidos[indice]['tempo_em_minutos'] + soma_total <= limiar):
        equacao_atual.append(pedidos[indice])
        descobre_variaveis(pedidos, equacao_atual.copy(), indice, limiar, menor_pedido)


def descobre_menor_pedido(pedidos):
    menor = pedidos[0]

    for i in range(0, len(pedidos)):
        if (pedidos[i]['tempo_em_minutos']):
            menor = pedidos[i]

    return menor

def e_mesmo_pedido(pedido, dado):
    if (pedido['quantidade'] == dado['quantidade'] and pedido['tempo_em_minutos'] == dado['tempo_em_minutos']):
        return True
    return False

def pega_multiplicador(pedido, variavel):
    multiplicador = 0

    for i in range(0, len(variavel)):
        dado = variavel[i]
        if (e_mesmo_pedido(pedido, dado)):
            multiplicador += 1
    return multiplicador

def gera_equacoes(pedidos, variaveis):
    equacoes = []

    for i in range(0, len(pedidos)):
        pedido = pedidos[i]
        equacao = []
        for j in range(0, len(variaveis)):
            variavel = variaveis[j]
            multiplicador = pega_multiplicador(pedido, variavel)
            equacao.append(f'{multiplicador}x{j+1}')
        equacoes.append(' + '.join(equacao) + ' >= ' + str(pedido['quantidade']))

    return equacoes     

variaveis = []
if __name__ == "__main__":
    tempo_maximo_dia = 540
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

    pedidos = sorted(pedidos, key=lambda k: k['tempo_em_minutos'], reverse=True) 
    
    menor_pedido = descobre_menor_pedido(pedidos)
    descobre_variaveis(pedidos, [], 0, tempo_maximo_dia, menor_pedido)

    equacoes = gera_equacoes(pedidos, variaveis)

    custo = []
    for i in range(0, len(variaveis)):
        custo.append(f'x{i + 1} ')
    
    print('min : ' + ' + '.join(custo)+";")
    for i in range(0, len(equacoes)):
        print(f'c{i + 1}: ' + equacoes[i]+";")
    for i in range(0, len(variaveis)):
        print(custo[i] + ' >= 0;')
