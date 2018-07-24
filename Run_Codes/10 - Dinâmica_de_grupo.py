entrada = list(map(lambda x: int(x),input().split()))
cod_disciplina = entrada[1::2]
num_matricula  = entrada[0::2]
def remove_repetidos(lista):
    disciplinas = []
    for i in lista:
        if i not in disciplinas:
            disciplinas.append(i)
    return disciplinas
saida = ''
solitarios = []
disciplinas = remove_repetidos(cod_disciplina)
dic = {}
for i in disciplinas:
    alunos = []
    for j in range(len(cod_disciplina)):
        if str(i) == str(cod_disciplina[j]):
            alunos.append(num_matricula[j])#lista auxiliar 
            dic[i] = alunos#Dicionário com os alunos cadastrados em cada disciplina
repeat = {}#Dicionário com o número de repetições de cada elemento
for i in range(len(num_matricula)):
    repeat[num_matricula[i]] = num_matricula.count(num_matricula[i])
for i in repeat.keys():
    if repeat[i] == 1:
        solitarios.append(i)#Elementos solitários
if solitarios == []:
    print(0)
else:
    rep = []
    lista = disciplinas #Lista para conferência da ordem em que aparecem as disciplinas
    for i in range(len(lista)):
            x = 0
            for j in solitarios:
                    for k in dic[lista[i]]:
                            if j == k:
                                    x+=dic[lista[i]].count(j)
            rep.append(x)#Número de vezes que um elemento repete em cada chave do dicionário
    frag = []
    maximo = max(rep)
    if rep.count(maximo) > 1: #Caso as disciplinas possuam o mesmo número de alunos solitários
        aux = []
        for i in range(rep.count(maximo)):
            aux+=[rep.index(maximo)]
            rep[rep.index(maximo)] = None#Para não perder a originalidade do index dos elementos
        saida = []
        for i in aux:
            saida+=[str(lista[i])]
        print(" ".join(saida))
    else:
        indice = rep.index(maximo)
        print(lista[indice])
   
