#Árvore para os livros
#Dados: Nome e Código
class NodeBook:
      def __init__(self, Nome, Código, Status):
            """Classe cria o objeto com os atributos nome e código"""
            self._nome = Nome
            self._codigo = Código
            self._status = Status
            self._cor = None
            self._filhoEsq = None
            self._filhoDir = None
            self._pai = None

      def getNome(self):
            return self._nome

      def getCodigo(self):
            return self._codigo

      def getStatus(self):
            return self._status

      def setStatus(self, newstatus):
            self._status = newstatus
