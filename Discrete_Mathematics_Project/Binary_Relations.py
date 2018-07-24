matriz, matriz1 = [], []
dominioR, imagemR, dominioS, imagemS = [], [], [], []

print()
print("#"*82,'|')
print("\t\t     __         __               ")
print("\t\t     ||         ||     ======      ")
print("\t\t     || =     = ||      ||    =     ")
print("\t\t     ||   = =   ||      ||    =     ")
print("\t\t     ||    =    ||      ||    =     ")
print("\t\tooo ====       ====    =======   ooo   \n")
print('|',"="*80,'|')
print("        Bem-vindo!Forneça um conjunto e realize operações com o mesmo!")
print('|',"="*80,'|')
print()

def reflexivaR():
      diagonal_principalR = ''
      for m in range(maximo):
           diagonal_principalR += matriz[m][m]
           
      if diagonal_principalR.count('1') == maximo:
           print("\nVerifiando se a relação R segue os parâmetros da propriedade reflexiva...A relação R é reflexiva")
                
      if diagonal_principalR.count('1') != maximo:
            print("\nVerifiando se a relação R segue os parâmetros da propriedade reflexiva...A relação R não é reflexiva")

def reflexivaS():
      diagonal_principalS = ''
      for ind in range(maximo):
           diagonal_principalS += matriz1[ind][ind]
           
      if diagonal_principalS.count('1') == maximo:
           print("\nVerifiando se a relação S segue os parâmetros da propriedade reflexiva... A relação S é reflexiva")
               
      if diagonal_principalS.count('1') != maximo:
           print("\nVerifiando se a relação S segue os parâmetros da propriedade reflexiva... A relação S não é reflexiva")

def antiReflexivaR():
    diagonal_principalR = ''
    for m in range(maximo):
        diagonal_principalR += matriz[m][m]
    if diagonal_principalR.count('0') == maximo:
        print("\nVerifiando se a relação R segue os parâmetros da propriedade anti-reflexiva...A relação R é anti-reflexiva")
                 
    if diagonal_principalR.count('0') != maximo:
        print("\nVerifiando se a relação R segue os parâmetros da propriedade anti-reflexiva...A relação R não é anti-reflexiva")

def antiReflexivaS():
    diagonal_principalS = ''
    for ind in range(maximo):
        diagonal_principalS += matriz1[ind][ind]
    if diagonal_principalS.count('0') == maximo:
        print("\nVerifiando se a relação S segue os parâmetros da propriedade anti-reflexiva... A relação S é anti-reflexiva")
               
    if diagonal_principalS.count('0') != maximo:
        print("\nVerifiando se a relação S segue os parâmetros da propriedade anti-reflexiva... A relação S não é anti-reflexiva")

def simetricaR(relacaoR):
    relacaoFormatada = auxiliarConverteTupla(relacaoR)
    count = 0
    for relacao in relacaoFormatada:
       for relacao1 in relacaoFormatada:
           if relacao != relacao1:
               print(relacao,relacao1)
               if relacao[0] == relacao[1]:
                   count+=1
                   break
               elif relacao == relacao1[::-1]:
                   count+=1
    if count == len(relacaoR):
        print("\nVerifiando se a relação R segue os parâmetros da propriedade simétrica... A relação R é simétrica")
    else:
        print("\nVerifiando se a relação R segue os parâmetros da propriedade simétrica... A relação R não é simétrica")

def simetricaS(relacaoS):
    relacaoFormatada = auxiliarConverteTupla(relacaoS)
    count = 0
    for relacao in relacaoFormatada:
       for relacao1 in relacaoFormatada:
           if relacao != relacao1:
               if relacao[0] == relacao[1]:
                   count+=1
               elif relacao == relacao1[::-1]:
                   count+=1
    if count == len(relacaoS):
        print(count)
        print("\nVerifiando se a relação S segue os parâmetros da propriedade simétrica... A relação S é simétrica")
    else:
        print("\nVerifiando se a relação S segue os parâmetros da propriedade simétrica... A relação S não é simétrica")

def dominioImagemR():
    global dominioR, imagemR
    cont = 0
    while cont < len(relacao):
        dominioR.append(int(relacao[cont][0])) #Adicionando elementos a lista de domínio da relação R
        imagemR.append(int(relacao[cont][2]))
        dominioR = list(set(dominioR))
        imagemR = list(set(imagemR))
        cont +=1

def dominioImagemS():
    global dominioS, imagemS
    cont = 0
    while cont < len(relacao1):
        dominioS.append(int(relacao1[cont][0]))#Adicionando elementos a lista de domínio da relacao S
        imagemS.append(int(relacao1[cont][2]))
        dominioS = list(set(dominioS))
        imagemS = list(set(imagemS))
        cont += 1

def imprimeMatriz(matriz):        
        for i in matriz:
            print(" ".join(i))
            continue

def auxiliarConverteTupla(relacao):
    a = set()
    for i in relacao:
        k = i.split(",")
        k = list(map(lambda x: int(x), k))
        a.add((k[0],)+(k[1],))
    return a

def RºS(relacao, relacao1):
    temp = set()
    for i in relacao:
        for j in relacao1:
            if int(i[2]) == int(j[0]):
                temp.add((int(i[0]),int(j[2])))
    return temp

def SºR(relacao, relacao1):
    temp = set()
    for i in relacao1:
        for j in relacao:
            if int(i[2]) == int(j[0]):
                temp.add((int(i[0]),int(j[2])))
    return temp

def retornarMaior(conjunto):
    sep = conjunto.split(',')
    sep = map(lambda x: int(x), sep)
    maximo = max(list(sep))#'maximo' range máximo da matriz
    
    return maximo

def validaRelacao(relacao, conjunto):
    maior = retornarMaior(conjunto)
    relacao = auxiliarConverteTupla(relacao)
    for i in relacao:
        if i[0] > maior or i[1] > maior:
            return False
            break
    return True

print("APENAS DIGITE TUPLAS QUE CONTENHAM NÚMEROS!\n")

while True:
    conjunto = input("Informe o conjunto a ser desenvolvido(OBS.: use vígula para separar os números. Caso queira alterar o conjunto reinicie o programa): ").strip()
    if conjunto == '':
        print("\n||||||Digite um conjunto válido!||||||\n")
        continue
    else:
        break
    
while True:
    relacaoR = input("\nDigite a relaçãoR(OBS.: use parênteses para separar os pares das relações e utilize vígulas para separá-los): ").strip()
    if relacaoR == '':
        print("\n||||||Digite uma relação válida!||||||")
        continue
    if not validaRelacao(relacaoR[1:-1].split('),('), conjunto):
        print("\n||||||Digite uma relação que coincida com os valores do conjunto!||||||")
        continue
    else:
        break
    
while True:
       relacaoS = input("\nDigite a relaçãoS(OBS.: use parênteses para separar os pares das relações e utilize vígulas para separá-los): ").strip()
       if relacaoS == '':
           print('\n||||||Digite uma relação válida!||||||\n')
           continue
       if not validaRelacao(relacaoS[1:-1].split('),('), conjunto):
            print("\n||||||Digite uma relação que coincida com os valores do conjunto!||||||")
            continue
       else:
            break

while True:
    maximo = retornarMaior(conjunto)
    relacao = relacaoR[1:-1].split('),(')
    relacao1 = relacaoS[1:-1].split('),(')

    def imprime_matriz():
         matriz = []
         for i in range(maximo): #Montagem da matriz
            lista = []
            for j in range(maximo):
                lista.append('0')
            matriz.append(lista)
         for i in range(maximo):
            for j in range(maximo):
                if maximo >= 4:
                 matriz[i][j] = str(matriz[i][j])
                else:
                    matriz[i][j] = str(matriz[i][j])
 
         y = 0
         while y < len(relacao): #Representação matricial da relacaoR
                matriz[int(relacao[y].split(',')[0])-1][int(relacao[y].split(',')[1])-1] = '1'
                y+=1
        
         return matriz
            
    
    def imprime_matriz1():
        matriz1 = []
        for i in range(maximo): #Representação matricial da relacaoS
            lista = []
            for j in range(maximo):
                lista.append("0")
            matriz1.append(lista)
        for i in range(maximo):
            for j in range(maximo):
                if maximo >= 4:
                 matriz1[i][j] = str(matriz1[i][j])
                else:
                    matriz1[i][j] = str(matriz1[i][j])
        x = 0
        while x < len(relacao1): #Adicionando 1 nas adjacências
                matriz1[int(relacao1[x].split(',')[0])-1][int(relacao1[x].split(',')[1])-1] = '1'
                x+=1

        return matriz1
        

    escolha = input("\nEscolha uma das opções abaixos:\n\n1 - Domínio e Imagem de R e S\n2 - Construa a matriz associada a R e S.\n3 - Verifique se R e S são relações reflexivas.\n4 - Verifique se R e S são anti-reflexivas\n5 - Verifique se R e S são relações simétricas\n6 - Obtenha SºR.\n7 - Obtenha RºS.\n8 - Sair\nForneça a operação desejada:")
    if escolha == '8':
        print("\n##Sessão finalizada!##")
        break
    if escolha == '1': #Dominio das relações R e S
        dominioImagemR()
        dominioImagemS()
            
        ######################################
        #Exibindo o conjunto domínio e imagem#
        ######################################

        print("\n Imprimindo o conjunto Domínio e Imagem das relações: ")
        print("\nDominio da relação R:  ",dominioR)
        print("\nImagem da relação R :  ",imagemR)
        print("\nDominio da relação S:  ",dominioS)
        print("\nImagem da relação S :  ",imagemS)
    y = 0
    if escolha == '2':
        matriz = imprime_matriz()
        matriz1 = imprime_matriz1()
        
        print('\nRepresentação matricial da relação R:\n')
        imprimeMatriz(matriz)
        print('\nRepresentação matricial da relação S:\n')
        imprimeMatriz(matriz1)
       
    if escolha == '3':
        matriz = imprime_matriz()
        matriz1 = imprime_matriz1()
        #Verificando se as relações são reflexivas
        reflexivaR()
        reflexivaS()

    if escolha == '4':
        matriz = imprime_matriz()
        matriz1 = imprime_matriz1()
        #Verificando se as relações são anti-reflexivas
        antiReflexivaR()
        antiReflexivaS()

    if escolha == '5':
        simetricaR(relacao)
        simetricaS(relacao1)

    if escolha == '6':
        print("\nConjunto resultante da operação SºR:")
        print("\nconjunto = " + str(SºR(relacao, relacao1)))

    if escolha == '7':
        print("\nConjunto resultante da operação RºS")
        print("\nconjunto = " + str(RºS(relacao, relacao1)))
        
