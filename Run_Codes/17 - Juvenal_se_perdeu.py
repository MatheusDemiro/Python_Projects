stringPre = ''
stringIn = ''
stringPost = ''
class TreeNode:
        def __init__(self, dados):
            self._dados = dados
            self._filhoEsq = None
            self._filhoDir = None
            self._pai = None

        def setFilhoEsq(self, nodoDir):
            self._filhoEsq = nodoDir

        def setFilhoDir(self, nodoEsq):
            self._filhoDir = nodoEsq

        def setPai(self, pai):
            self._pai = pai

        def setDados(self, novodados):
                self._dados = novodados
        
        def getPai(self):
            return self._pai

        def getFilhoEsq(self):
            return self._filhoEsq

        def getFilhoDir(self):
            return self._filhoDir

        def getDados(self):
            return self._dados

class Tree(TreeNode):
    def __init__(self):
        self._raiz = None

    def setRaiz(self, nodeRaiz):
        self._raiz = nodeRaiz

    def getRaiz(self):
        return self._raiz             
    
    def PesquisarNodo(self, nodo):
            aux = self._raiz
            if nodo == None:
                    return False
            while aux.getDados()!= nodo.getDados():
                if aux.getDados() > nodo.getDados():
                    aux = aux.getFilhoEsq()
                    if aux == None:
                        return False
                else:
                    aux = aux.getFilhoDir()
                    if aux == None:
                        return False
            else:
                   return aux
 
    def InserirNodo(self, nodo):
        aux = None
        x = self._raiz
        while x != None:
            aux = x
            if x.getDados() >= nodo.getDados():
                x = x.getFilhoEsq()
            else:
                x = x.getFilhoDir()
        nodo.setPai(aux)
        if aux == None:
            self._raiz = nodo
        else:
            if nodo.getDados() <= aux.getDados():
                aux.setFilhoEsq(nodo)
            else:
                aux.setFilhoDir(nodo)
    
    def PreOrder(self, nodo):
            global stringPre
            if nodo != None:
                    stringPre+=' '+format((nodo.getDados()))
                    self.PreOrder(nodo.getFilhoEsq())
                    self.PreOrder(nodo.getFilhoDir())


    def InOrder(self, nodo):
           global stringIn
           if nodo != None:
                self.InOrder(nodo.getFilhoEsq())
                stringIn+=' '+format(nodo.getDados())
                self.InOrder(nodo.getFilhoDir())
                
    def PosOrder(self,nodo):
            global stringPost
            if nodo != None:
                self.PosOrder(nodo.getFilhoEsq())
                self.PosOrder(nodo.getFilhoDir())
                stringPost+=' '+format(nodo.getDados())

    def MaiorFilhoEsq(self,nodo):#Menor elemento da subárvore esquerda de um nodo qualquer
        while nodo.getFilhoEsq() != None:#pesquisar pela direita
                nodo = nodo.getFilhoEsq()
        return nodo

    def MaiorFilhoDir(self,nodo):#Menor elemento da subárvore direita de um nodo qualquer
        while nodo.getFilhoDir() != None:
                nodo = nodo.getFilhoDir()                        
        return nodo

    def MaiorMenor(self, nodo): #Maior valor da árvore que é menor que o nodo, se não existir imprima 0
            aux = self._raiz#5
            if aux == None:
                    return 0
            else:
                    if nodo.getDados() > aux.getDados():
                            if nodo.getPai() == aux and nodo.getFilhoEsq is None:
                                    return aux
                            elif nodo.getFilhoEsq() != None:
                                    return nodo.getPai()
                            else:
                                    return nodo.getPai()                   
                           
                    elif nodo.getDados() < aux.getDados():
                            if nodo.getFilhoEsq() is not None:
                                    return nodo.getFilhoEsq()
                            else:
                                    return 0
                    elif aux.getFilhoEsq() != None:
                            return self.MaiorFilhoDir(aux.getFilhoEsq())
                    else:
                            return self.MaiorFilhoEsq(aux.getFilhoDir())

    def Predecessor(self,nodo):
            if nodo.getFilhoEsq() != None:
                    return self.MaiorFilhoDir(nodo.getFilhoEsq())
            else:
                    aux = nodo.getPai()
                    while aux != None and nodo == aux.getFilhoEsq():
                            nodo = aux
                            aux = aux.getPai()
                    return aux

    def Sucessor(self,nodo):
            if nodo.getFilhoDir() != None:
                    return self.MaiorFilhoEsq(nodo.getFilhoDir())
            aux = nodo.getPai()
            while aux != None and nodo == aux.getFilhoDir():
                    nodo = aux
                    aux = aux.getPai()
            return aux
                            
            
    def Remover(self, nodo):#nodo folha; nodo com 1 filho; nodo com 2 filhos
        if self.PesquisarNodo(nodo) != False:
                        aux = self._raiz
                        if aux == None:
                          return None
                        elif aux.getDados() == nodo.getDados() and aux.getFilhoEsq() != None:
                                var = self.MaiorMenor(nodo)
                                if var.getFilhoEsq() == None and var.getFilhoDir() == None:
                                        self.setRaiz(var)
                                        (var.getPai()).setFilhoDir(None)
                                elif var.getFilhoEsq() != None and var.getFilhoDir() == None:
                                        j = var.getPai()
                                        j.setFilhoDir(var.getFilhoEsq())
                                        var.setFilhoDir(aux.getFilhoDir())
                                        var.setFilhoEsq(aux.getFilhoEsq())
                                        self.setRaiz(var)
                        elif aux.getDados() == nodo.getDados() and aux.getFilhoEsq() == None:
                                j = var.getPai()
                                j.setFilhoDir(None)
                                var = self.MaiorMenor(nodo)
                                var.setFilhoDir(aux.getFilhoDir())
                                self.setRaiz(var)
                                
                        elif nodo.getFilhoEsq() == None and nodo.getFilhoDir() == None:
                              var = nodo.getPai()
                              if var.getDados() <= nodo.getDados():
                                      var.setFilhoDir(None)
                              else:
                                      var.setFilhoEsq(None)
                        elif nodo.getFilhoEsq() == None and nodo.getFilhoDir() != None:
                                var = nodo.getPai()
                                direito = nodo.getFilhoDir()
                                if var.getDados() >= direito.getDados():
                                        var.setFilhoEsq(direito)
                                else:
                                        var.setFilhoDir(direito)
                        elif nodo.getFilhoEsq() != None and nodo.getFilhoDir() == None:
                                var = nodo.getPai()
                                esquerdo = nodo.getFilhoEsq()
                                if var.getDados() > esquerdo.getDados():
                                        var.setFilhoEsq(esquerdo)
                                else:
                                        var.setFilhoDir(esquerdo)
                        else:
                                var = self.MaiorMenor(nodo)
                                if var.getFilhoEsq() == None and var.getFilhoDir() == None:
                                        j = nodo.getPai()
                                        j.setFilhoEsq(nodo.getFilhoEsq())
                                        var.setFilhoDir(nodo.getFilhoDir())

#Estruturado
arvore = Tree()
entrada = input().split()
saida = ''
lista = []
objetos = []
for i in range(len(entrada)):
        if entrada[i] == 'I':
                nodo = TreeNode(int(entrada[i+1]))
                objetos.append(nodo)
                arvore.InserirNodo(nodo)
        elif entrada[i] == 'Q':
                if arvore.getRaiz() == None:
                        lista.append(" 0")
                else:
                        nodo = arvore.PesquisarNodo(TreeNode(int(entrada[i+1])))
                        aux = arvore.MaiorMenor(nodo).getDados()
                        lista.append(" "+str(aux))
        elif entrada[i] == 'R':
                nodo = arvore.PesquisarNodo(TreeNode(int(entrada[i+1])))
                arvore.Remover(nodo)
        elif entrada[i] ==  'PRE':
                arvore.PreOrder(arvore.getRaiz())
                if stringPre == '':
                        lista.append(' 0')
                else:
                        lista.append("".join(stringPre))
        elif entrada[i] == 'POST':
                arvore.PosOrder(arvore.getRaiz())
                if stringPost == '':
                        lista.append(' 0')
                else:
                        lista.append("".join(stringPost))
        elif entrada[i] == 'IN':
                arvore.InOrder(arvore.getRaiz())
                if stringIn == '':
                        lista.append(' 0')
                else:
                        lista.append("".join(stringIn))
lista[0] = lista[0].lstrip()
print(";".join(lista)+';')
