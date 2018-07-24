entrada = input().split(";")[0:-1]
dic = {}
saida = ''
for i in range(len(entrada)):
      string = ''
      if entrada[i][0] == 'A':
            for j in entrada[i][2:]:
                  if j == ':':
                        aux = entrada[i][entrada[i].index(":")+1:]
                        break
                  string+=j
            if string in dic.keys():
                  if type(dic[string]) is str:
                        dic[string] = [dic[string],aux]
                  else:
                        dic[string].append(aux)
            else:                  
                  dic[string] = aux
      if entrada[i][0] == 'R':
            del dic[entrada[i][2:]]
      if entrada[i][0] == 'B':
            if entrada[i][2:] not in dic.keys():
                  saida+='oxente?'+';'
            elif type(dic[entrada[i][2:]]) is list: 
                  saida+="+".join(dic[entrada[i][2:]])+';'
            else:
                  saida+=dic[entrada[i][2:]]+';'
print(saida)
