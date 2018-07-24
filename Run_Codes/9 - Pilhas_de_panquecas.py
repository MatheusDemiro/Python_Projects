def pilha_ordenada(pilha):
	casos = 0
	for i in range(len(pilha)-1):
		if pilha[i] > pilha[i+1]:
			casos+=1
			if casos > 0:
				return False
	if casos == 0:
		return True
def vira (ind):
    return ind[::-1]
def maior_elemento(pilha):
    return max(pilha)
def minimo_elemento(pilha):
    return min(pilha)
def base(pilha):
    return pilha[-1]
def topo(pilha):
    return pilha[0]
def remover_base(pilha):
    base = pilha[-1]
    aux = []
    for i in pilha[::-1]:
        if i != base:
            var = pilha.pop(pilha.index(i))
            aux.append(var)
        else:
            pilha.pop(pilha.index(i))
    return aux[::-1]            
saida = ''
temp = []
entrada = list(map(lambda x: int(x),input().split()))
pilha = [int(x) for x in entrada]
var = pilha[::]
fatia = pilha[::]
while True:
    if pilha_ordenada(pilha):
            print('0')
            break
    if pilha_ordenada(fatia):
        saida = saida+'0'
        print(" ".join(saida))
        break
    maior = maior_elemento(fatia)
    minimo = minimo_elemento(fatia)
    if maior in temp:
        if len(temp) <= 1:
            var =fatia[:fatia.index(maior)]
        else:
            var = fatia[:fatia.index(maior)-(len(temp)-1)]
        if pilha_ordenada(fatia+temp):
            print(" ".join(saida))
            break
        top = topo(var)
        ba = base(var)
        maior = maior_elemento(var)
        if maior == top:
            t = var[::]#t = fatia[fatia.index(maior):]
            ind = fatia[::-1].index(t[-1])+1 #t[0]
            saida = saida+str(ind) #fatia[::-1].index(t[-1])+1
            t = t[::-1]
            for i in range(len(fatia[:len(t)])):
                fatia[i] = t[i]
            temp = [maior] + temp
            continue
        elif maior == ba:
            temp = [maior] + temp
            continue
        else:
            t = var[:var.index(maior)+1]
            ind = fatia[::-1].index(max(t)) + 1
            saida = saida+str(ind)
            t = t[::-1]
            for i in range(len(fatia[::-1][ind-1:])):
               fatia[i] = t[i]
            continue

    else:
        x = fatia[:fatia[::-1].index(maior)+1]
        top = topo(fatia)
        if maior == top:
            ind = fatia.index(x[-1]) + 1 
            saida = saida+str(ind - fatia.index(fatia[-1]))
            t = x[::]
            t = t[::-1]
            for i in range(len(fatia[:ind])):
                fatia[i] = t[i]
            temp = [maior]+temp
            continue
        else:
            if fatia.index(maior) > 1 :
                    x = fatia[:fatia[::-1].index(maior)+2]
                    t = x[::]
                    ind = fatia[::-1].index(t[-1])+1
                    saida = saida+str(ind)
                    t = t[::-1]
                    for i in range(len(fatia[:ind+1])):
                        fatia[i] = t[i]
                    continue
            else:
                    x = fatia[:fatia[::-1].index(maior)]
                    t = x[::]
                    ind = fatia[::-1].index(t[-1])+1
                    saida = saida+str(ind)
                    t = t[::-1]
                    for i in range(len(fatia[:ind-1])):
                        fatia[i] = t[i]
                    continue
