from TreeNode import TreeNode
class Tree:
      def __init__(self):
            self._root = None
            self._guard_node = []#Lista que guarda os nodos inseridos na árvore
            
      def getRoot(self):
            return self._root

      def setRoot(self, newroot):
            self._root = newroot
            self._guard_node.append(self._root)#Adicionando a raiz diretamente a lista

      def getObjects(self):#Método que retorna lista de nodos
            return self._guard_node

      def InsertNodeRight(self, nodo1, nodo2):
          nodo1.setSonRight(nodo2)
          if nodo2.getTextNode() != None:#Se não for um nodo folha adicione a lista
                self._guard_node.append(nodo2)          

      def InsertNodeLeft(self, nodo1, nodo2):
          nodo1.setSonLeft(nodo2)
          if nodo2.getTextNode() != None:#Se não for um nodo folha adicione a lista
                self._guard_node.append(nodo2)

      def LastNode(self):#Retorne o último objeto inserido na árvore
            return self._guard_node[-1]
      
      def SearchNode(self, node):#Pesquisando pelo nodo desejado, caso o mesmo não seja encontrado na lista de objetos inseridos na árvore, retorne None. 
            node = node.split()
            for element in range(len(self._guard_node)):
                  if self._guard_node[element].getIdNode() == node[2] and self._guard_node[element].getTextNode() == node[0]:#Se texto e id forem iguais, então retorne o nodo achado na árvore
                        temp = self._guard_node[element]
                        del self._guard_node[element]#Quando o elemento for achado retire-o da lista
                        return temp
            return None
