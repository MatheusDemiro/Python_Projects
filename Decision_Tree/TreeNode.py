#Class para criar o nodo com as características requeridas (texto, sinal e id).
#Considera-se as variáveis(a1,a6,...) como sendo o texto e o número float o seu id.
class TreeNode:
      def __init__(self, textNode, signNode, idNode):
            self._textNode = textNode
            self._idNode = idNode
            self._signNode = signNode
            self._sonLeft = None
            self._sonRight = None
            self._father = None

      def getIdNode(self):
            return self._idNode

      def getTextNode(self):
            return self._textNode

      def getSignNode(self):
            return self._signNode
      
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
