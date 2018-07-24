string = ''
class Node:
      def __init__(self, data):
            self._data = data
            self._sonLeft, self._sonRight = None, None
            self._father = None

      def getData(self):
            return self._data
      
      def getFather(self):
            return self._father

      def getSonLeft(self):
            return self._sonLeft

      def getSonRight(self):
            return self._sonRight

      def setFather(self, newfather):
            self._father = newfather            

      def setSonLeft(self, newleft):
            self._sonLeft = newleft

      def setSonRight(self, newright):
            self._sonRight = newright

      def setData(self,newdata):
            self._data = newdat 

            
class TreeAvl:
      def __init__(self):
            self._nil = Node(None)
            self._root = self._nil
            
      def getRoot(self):
            return self._root

      def setRoot(self, newroot):
            self._root = newroot

      def RotateLeft(self,node):
            aux = node.getSonRight()
            node.setSonRight(aux.getSonLeft())
            if aux.getSonLeft() != self._nil:
                  aux.getSonLeft().setFather(node)
            aux.setFather(node.getFather())
            if node.getFather() == self._nil:
                  self.setRoot(aux)
            else:
                  if node == node.getFather().getSonLeft():
                        node.getFather().setSonLeft(aux)
                  else:
                        node.getFather().setSonRight(aux)
            aux.setSonLeft(node)
            node.setFather(aux)

      def RotateRight(self, node):
            aux = node.getSonLeft()
            node.setSonLeft(aux.getSonRight())
            if aux.getSonRight() != self._nil:
                  aux.getSonRight().setFather(node)
            aux.setFather(node.getFather())
            if node.getFather() == self._nil:
                  self.setRoot(aux)
            else:
                  if node == node.getFather().getSonRight():
                        node.getFather().setSonRight(aux)#Setando o filho direito do pai do nodo para aux
                  else:
                        node.getFather().setSonLeft(aux)#Setando o filho esquerdo do pai do nodo para aux
            aux.setSonRight(node)
            node.setFather(aux)         
            
      def Height(self, node):
            if node == self._nil:
                  return -1
            h1 = self.Height(node.getSonLeft())
            h2 = self.Height(node.getSonRight())
            return (1+max(h1,h2))                

      def FactorBalance(self, node):
            if node == None or node == self._nil:
                  return -1
            else:
                  fact1 = self.Height(node.getSonLeft())
                  fact2 = self.Height(node.getSonRight())
                  return fact1 - fact2#Altura da sub-árvore esquerda - Altura da sub-árvore direita

      def InOrder(self,node):
            global string
            if node != self._nil:
                  self.InOrder(node.getSonLeft())
                  string+=str((node.getData()))+' '
                  self.InOrder(node.getSonRight())         

      def Degree(self, node):
            aux = self._root
            if node == self.getRoot():
                  return 1
            elif node == self._nil:
                  var=-1
                  return -1
            else:
                  var = 1
                  while aux.getData() != node.getData():
                        if aux.getData() > node.getData():#Pesquisar à esquerda
                              aux = aux.getSonLeft()
                              var+=1
                              if aux == self._nil:
                                    return -1
                        else:
                              aux = aux.getSonRight()
                              var+=1
                              if aux == self._nil:
                                    return -1
                  else:
                        return var

      def ReadBalance(self, node):
            #Se o fb for negativo, então pegamos o filho da direita. Caso o filho da direita for positivo usamos uma rotação dupla à esquerda.
            #Caso o filho da direita for negativo usamos uma rotação simples à esquerda.
            #Se o fb for positivo, então pegamos o filho da esquerda. Caso o fb do filho da esquerda seja negativo usamos uma rotação dupla à direita.
            #Caso o filho da esquerda seja positivo usamos uma rotação simples à direita.
            balance = self.FactorBalance(node)
            if balance > 1 or balance < -1:
                        if self.FactorBalance(node) < 0:
                              if self.FactorBalance(node.getSonRight()) < 0:#Fb do node negativo e fb do filho direito do node negativo.
                                    self.RotateLeft(node)
                              else:
                                    self.RotateRight(node.getSonRight())#Dupla rotação à Esquerda (Fb do node negativo e fb do filho direito do node positivo).
                                    self.RotateLeft(node)
                        else:
                              if self.FactorBalance(node.getSonLeft()) < 0:#Fb do node positivo e fb do filho esquerdo do node negativo.
                                    self.RotateLeft(node.getSonLeft())#Dupla rotação à Direita.
                                    self.RotateRight(node)
                              else:
                                    self.RotateRight(node)
            elif node.getFather() != self._nil:
                  self.ReadBalance(node.getFather())            

      def InsertNode(self, node):
            aux = self._nil
            temp = self.getRoot()
            if temp == self._nil:
                  temp = self._nil
            while temp != self._nil:
                       aux = temp
                       if temp.getData() < node.getData():
                             temp = temp.getSonRight()
                       else:
                              temp = temp.getSonLeft()
            node.setFather(aux)
            if aux == self._nil:
                  self.setRoot(node)
            else:
                  if node.getData()  < aux.getData():
                              aux.setSonLeft(node)
                  else:
                              aux.setSonRight(node)
            node.setSonRight(self._nil)
            node.setSonLeft(self._nil)
            self.ReadBalance(node)

      def SearchNode(self, node):
            aux = self._root
            if aux.getData()==None:
                  return self._nil
            else:
                  if node == None:
                          return self._nil
                  while aux.getData() != node.getData(): 
                      if aux.getData() > node.getData():
                          aux = aux.getSonLeft()
                          if aux == self._nil:
                              return self._nil
                      else:
                          aux = aux.getSonRight()
                          if aux == self._nil:
                              return self._nil
                  else:
                         return aux

entrada = input().split('#')
if entrada[-1] == '':
      del entrada[-1]
saida = ''
for i in range(len(entrada)):
      arvore = TreeAvl()
      temp = entrada[i].split()
      saida = saida[0:-1] + "#"
      l = []
      for j in range(len(temp)):
            if temp[j] == 'I':
                  arvore.InsertNode(Node(int(temp[j+1])))
            elif temp[j] == 'N':
                  saida+=(str(arvore.Degree(Node(int(temp[j+1])))))+'@'

            elif temp[j] == 'L':
                  lista = []
                  string = ''
                  string = string[0:-1]
                  node1 = (Node(int(temp[j+1])))
                  node2 = (Node(int(temp[j+2])))
                  arvore.InOrder(arvore.getRoot())
                  string = string.split()
                  if str(node1.getData()) not in string and str(node2.getData()) not in string:
                        saida+='-1'
                  else:
                        if str(node1.getData()) in string and str(node2.getData()) in string:
                              if node1.getData() == node2.getData():
                                    pos1 = string.index(str(node1.getData()))
                                    saida+=" ".join(string[pos1:pos1+1])+'@'
                              else:
                                    pos1 = string.index(str(node1.getData()))
                                    pos2 = string.index(str(node2.getData()))
                                    saida+=" ".join(string[pos1:pos2+1])+'@'
                        elif str(node1.getData()) in string:
                              pos1 = string.index(str(node1.getData()))
                              saida+=" ".join(string[:pos1+1])+'@'
                        elif str(node2.getData()) in string:
                              pos2 = string.index(str(node2.getData()))
                              saida+=" ".join(string[:pos2+1])+'@'
print(saida[1:-1])  
