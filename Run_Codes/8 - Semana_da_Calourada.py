def bubble_sort(lista):
    trocas = 0
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
                trocas+=1
            else:
                pass
    print(trocas)

entrada = list(map(lambda x: int(x),input().split()))
qtd_estudantes = entrada.pop(0)
bubble_sort(entrada)
                
                
                
