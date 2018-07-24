entrada = input().split('-')
total = entrada.pop(0).split()

def formatando(entrada):
    dados = []
    for i in range(len(entrada)):
        aux = list(map(lambda x: int(x),entrada[i].strip().split()))
        aux.reverse()
        dados.append(tuple(aux))
    return dados

def topo(dados):
    for i in dados:
        if i[0] == 1:
            return True
def elemento_1(dados):#posição do elemento 1 na lista
    for i in range(len(dados)):
        if 1 in dados[i]:
            return i

def posicao_1(i,dados):#posicão do elemento 1 na tupla
    for j in dados[i]:
        if j == 1:
            return dados[i].index(j)

dados = formatando(entrada)
if topo(dados):
    print(0)
else:
    elements = 0
    tamanho = len(dados)
    indice = elemento_1(dados)
    position = posicao_1(indice,dados)
    for i in range(len(dados)):
        if i == indice-1:
            if len(dados[indice]) > len(dados[indice-1]):
                elements+=(len(dados[indice])-len(dados[indice-1]))+(position-1)
            elif len(dados[indice]) < len(dados[indice-1]):
                elements+=(len(dados[indice-1])-len(dados[indice]))+(position+1)
            else:
                elements+=(len(dados[indice])+len(dados[indice-1]))-1
        if i == indice:
            elements+=position
        if i == indice+1:
            if len(dados[indice]) > len(dados[indice+1]):
                elements+=(len(dados[indice])-len(dados[indice+1]))+(position-1)
            elif len(dados[indice+1]) > len(dados[indice]):
                elements+=(len(dados[indice+1])-len(dados[indice])+(position+1))
            else:
                elements+=(len(dados[indice])+len(dados[indice+1]))-1
    print(elements)
