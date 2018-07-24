#Classe de construção dos nodos
class Node:
      def __init__(self, Dados):
            self._dados = Dados          
            self._cor = None
            self._filhoEsq = None
            self._filhoDir = None
            self._pai = None

      def setFilhoEsq(self, nodoDir):
            self._filhoEsq = nodoDir

      def setFilhoDir(self, nodoEsq):
            self._filhoDir = nodoEsq

      def setPai(self, pai):
            self._pai = pai

      def setCor(self,novacor):
              self._cor = novacor
            
      def getPai(self):
            return self._pai

      def getFilhoEsq(self):
            return self._filhoEsq

      def getFilhoDir(self):
            return self._filhoDir

      def getCor(self):
            return self._cor

      def getDados(self):
            return self._dados
