entrada = input().split()
retangulo_1 = tuple(map(lambda x : int(x),entrada[0:4]))
retangulo_2 = tuple(map(lambda x: int(x),entrada[4:]))
def saida(retangulo_1,retangulo_2):
    if retangulo_1[2:4] >= retangulo_2[0:3]:
        print(1)
    else:
        print(0)
saida(retangulo_1,retangulo_2)
