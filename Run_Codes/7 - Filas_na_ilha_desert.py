def bubbleSort(idades):
    if len(idades) <= 1:
        sidades = idades
    else:
        for j in range(0,len(idades)):
            for i in range(0,len(idades)-1):
                if idades[i]<idades[i+1]:
                    copy = idades[i+1]
                    idades[i+1] = idades[i]
                    idades[i] = copy
        sidades = idades

    return sidades


entrada = input().split(",")
idades,nomes, saida = [],[],[]
l = []
for i in range(len(entrada)):
    entrada[i] = entrada[i].lstrip()
for i in range(len(entrada)):
    if entrada[i].isdigit():
        idades.append(int(entrada[i]))
    else:
        nomes.append(entrada[i])
for i in range(len(idades)):
    l.append((nomes[i],idades[i]))
idades = bubbleSort(idades)
finish = []
for i in idades:
    for j in l:
        if j[1] == i and j[0] not in finish:
            finish.append(j[0])
print(",".join(finish))
