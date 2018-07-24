entrada = list(map(lambda x: int(x),input().split()))
time1 = entrada[0:2]
time2 = entrada[2:]
y = [min(time1),max(time2)]
x = [max(time1),min(time2)]
print(abs(sum(x)-sum(y)))

for i in range(len(entrada)):
    menores = [min(entrada)]
    del entrada[entrada.index(min(entrada))]



            


