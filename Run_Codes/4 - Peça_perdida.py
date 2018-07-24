lista = list(map(lambda x: int(x),input().split()))
for i in range(1,lista[0]):
    if i not in lista:
        print(i)
