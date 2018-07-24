entrada = list(map(lambda x: int(x), input().split()))
finish = []
for i in entrada:
    lista = []
    emp = 2
    x = 0
    def garrafas_refrigerante(num):
        global lista
        global emp
        global x
        global finish
        if x == 0 and num % 2 == 0:
            lista.append(num)
            num+=1
            emp-=1
            return garrafas_refrigerante(num)
        x+=1
        if num == 1 and emp == 0:
            finish.append(str(sum(lista)))
        else:
                if num % 2 != 0:
                    num_garrafas = num//3 #trios de garrafa
                    if num_garrafas == 0:
                        lista.append(num_garrafas)
                        if i % 2 == 1:
                            lista.append(i)
                        finish.append(str(sum(lista)))
                    sobra = num%3 #sobra de garrafas
                    lista.append(num_garrafas)
                    if sobra + num_garrafas >= 3:
                        num_garrafas = (sobra+num_garrafas)//3
                        lista.append(num_garrafas)
                        return(garrafas_refrigerante(num_garrafas))
                    return garrafas_refrigerante(num_garrafas)
                else:
                    num_garrafas = num//3
                    sobra = num%3
                    if num_garrafas !=0:
                        lista.append(num_garrafas)
                        return garrafas_refrigerante(num_garrafas)
                    if sobra > 0:
                        dec = 3-sobra
                        emp-=dec
                        num_garrafas+=dec
                        lista.append(num_garrafas)
                        return garrafas_refrigerante(num_garrafas)
    garrafas_refrigerante(i)            
print(" ".join(finish))
