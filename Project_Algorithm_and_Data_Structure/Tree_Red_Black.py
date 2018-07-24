from Node_Livros import NodeBook
from Node_Usuarios import NodeUser
from Node import Node

class Tree:
      def __init__(self):
            self._nil = Node(None)
            self._nil.setCor('preto')
            self._raiz = self._nil
            self._armazena = None#Variável auxiliar
            self._lista = []

      def setRaiz(self, novaRaiz):
            self._raiz = novaRaiz

      def setLista(self):#Esvaziando a lista com os dados solitados pelo método BookCds ou CpfCds
            self._lista = []
            
      def getRaiz(self):
            return self._raiz
      
      def getLista(self):#Método que retorna a lista com os dados que forem solicitados de cpfs cadastrados ou livros cadastrados
            self._armazena = self._lista[::]#Variável que recebe uma cópia da lista ordenada (InOrder) dos nodos presentes na árvore
            self.setLista()#Apagando os dados da lista para evitar colisão de dados
            return self._armazena
      
      def MenorSub(self,nodo):#Selecionando o nodo mínimo a partir de um determinado nodo
          while nodo.getFilhoEsq() != self._nil:#Se o nodo não possui subárvore esquerda, então, visto que todo nó da subárvore direita é maior do que o nodo, o nó mínimo será o próprio nodo de entrada.
                nodo = nodo.getFilhoEsq()                        
          return nodo

      def RotacaoEsq(self,nodo):
            aux = nodo.getFilhoDir()
            nodo.setFilhoDir(aux.getFilhoEsq())
            if aux.getFilhoEsq() != self._nil:
                  aux.getFilhoEsq().setPai(nodo)
            aux.setPai(nodo.getPai())
            if nodo.getPai() == self._nil:
                  self.setRaiz(aux)
            else:
                  if nodo == nodo.getPai().getFilhoEsq():
                        nodo.getPai().setFilhoEsq(aux)#Setando o filho esquerdo do pai do nodo para aux
                  else:
                        nodo.getPai().setFilhoDir(aux)#Setando o filho direito do pai do nodo para aux
            aux.setFilhoEsq(nodo)
            nodo.setPai(aux)
            
      def RotacaoDir(self, nodo):
            aux = nodo.getFilhoEsq()
            nodo.setFilhoEsq(aux.getFilhoDir())
            if aux.getFilhoDir() != self._nil:
                  aux.getFilhoDir().setPai(nodo)
            aux.setPai(nodo.getPai())
            if nodo.getPai() == self._nil:
                  self.setRaiz(aux)
            else:
                  if nodo == nodo.getPai().getFilhoDir():
                        nodo.getPai().setFilhoDir(aux)#Setando o filho direito do pai do nodo para aux
                  else:
                        nodo.getPai().setFilhoEsq(aux)#Setando o filho esquerdo do pai do nodo para aux
            aux.setFilhoDir(nodo)
            nodo.setPai(aux)

      def InserirNodo(self,nodo):#Método de inserção dos nodos e ordenação através do nome
            aux = self._nil
            var = self._raiz#var recebe raiz
            if var == None:#Se árvore estiver vazia var recebe o nodo sentinela
                 var = self._nil
            while var != self._nil:
                  aux = var
                  if nodo.getDados().getNome() < var.getDados().getNome():#Comparando pelo nome
                        var = var.getFilhoEsq()
                  else:
                        var = var.getFilhoDir()
            nodo.setPai(aux)
            if aux == self._nil:#Caso a raiz esteja com o nodo sentinela, ou seja, vazia
                  self.setRaiz(nodo)#Setando a raiz para o primeiro nodo a ser inserido na árvore
            else:
                  if nodo.getDados().getNome() < aux.getDados().getNome():
                        aux.setFilhoEsq(nodo)
                  else:
                        aux.setFilhoDir(nodo)
            nodo.setFilhoEsq(self._nil)
            nodo.setFilhoDir(self._nil)
            nodo.setCor('vermelho')#Todo nodo tem a sua cor inicial setada para vermelho.
            self.InserirReparar(nodo)#Chamando método InserirReparar responsável por manter as características da árvore vermelho preto.

      def InserirReparar(self, nodo):#Método que corrige as cores dos nodos após uma inserção, pois podem ocorrer violações nas propriedades 2(raiz deve ser preta) e 4(se um nó é vemelho seus filhos são pretos).
                  while nodo.getPai().getCor() == 'vermelho':
                        if nodo.getPai() == nodo.getPai().getPai().getFilhoEsq():#Se o pai do nodo for igual ao filho esquerdo do avô
                              aux = nodo.getPai().getPai().getFilhoDir()#aux recebe o filho direito do avô do nodo
                              if aux.getCor() == 'vermelho':
                                    nodo.getPai().setCor('preto')
                                    aux.setCor('preto')
                                    nodo.getPai().getPai().setCor('vermelho')
                                    nodo = nodo.getPai().getPai()
                              else:#Se o filho direito do avô do nodo não for vermelho
                                    if nodo == nodo.getPai().getFilhoDir():#Se nodo estiver a direita do seu pai
                                          nodo = nodo.getPai()
                                          self.RotacaoEsq(nodo)
                                    nodo.getPai().setCor('preto')
                                    nodo.getPai().getPai().setCor('vermelho')
                                    self.RotacaoDir(nodo.getPai().getPai())
                        else:
                              aux = nodo.getPai().getPai().getFilhoEsq()#aux recebe o filho esquerdo do avô do nodo
                              if aux.getCor() == 'vermelho':#Se aux(primo do nodo) for igual a vermelho
                                    nodo.getPai().setCor('preto')
                                    aux.setCor('preto')
                                    nodo.getPai().getPai().setCor('vermelho')
                                    nodo = nodo.getPai().getPai()
                              else:
                                    if nodo == nodo.getPai().getFilhoEsq():
                                          nodo = nodo.getPai()
                                          self.RotacaoDir(nodo)
                                    nodo.getPai().setCor('preto')
                                    nodo.getPai().getPai().setCor('vermelho')
                                    self.RotacaoEsq(nodo.getPai().getPai())                              
                  self._raiz.setCor('preto')

      def Transplante(self,nodo1,nodo2):#Seleciona o maior elemento da subárvore esquerda. Caso esta encontra-se vazia o menor elemento da subárvore direita será selecionado para transplante.
            if nodo1.getPai() == self._nil:#nodo1 que será retirado e dará lugar ao nodo2.
                  self.setRaiz(nodo2)#nodo2 nodo selecionado para assumir a posição do nodo1.
            else:
                  if nodo1 == nodo1.getPai().getFilhoEsq():#Se nodo1 for filho esquerdo do pai
                        nodo1.getPai().setFilhoEsq(nodo2)#Então setamos o filho esquerdo pai para o nodo2
                  else:
                        nodo1.getPai().setFilhoDir(nodo2)
            nodo2.setPai(nodo1.getPai())

      def RemoverNodo(self,nodo):#Removendo nodo da árvore.
            guard = nodo
            cor_original = guard#Guardando a cor original do nodo.
            if nodo.getFilhoEsq() == self._nil:
                  aux = nodo.getFilhoDir()
                  self.Transplante(nodo, nodo.getFilhoDir())#Se filho esquerdo do nodo de entrada for o nó sentinela, então utilize o método Transplante entrando nodo1 = nodo e nodo2 = filho direito do nodo de entrada.
            else:# Se filho esquerdo do nodo for diferente de nil
                  if nodo.getFilhoDir() == self._nil:
                        aux = nodo.getFilhoEsq()
                        self.Transplante(nodo, nodo.getFilhoEsq())#Chamando o método transplante com nodo1 = nodo e nod2 = filho esquerdo do nodo de entrada.
                  else:
                        guard = self.MenorSub(nodo.getFilhoDir())#Seleção do maior filho à esquerda da árvore.
                        cor_original.setCor(guard.getCor())#Setando a cor_original do nodo para a cor do marios filho à esquerda da árvore.
                        aux = guard.getFilhoDir()
                        if guard.getPai() == nodo:
                              aux.setPai(guard)
                        else:
                              self.Transplante(guard, guard.getFilhoDir())
                              guard.setFilhoDir(nodo.getFilhoDir())
                              guard.getFilhoDir().setPai(guard)
                        self.Transplante(nodo, guard)
                        guard.setFilhoEsq(nodo.getFilhoEsq())
                        guard.getFilhoEsq().setPai(guard)
                        guard.setCor(nodo.getCor())
                        
            if cor_original == 'preto':
                  self.RemoverReparar(x)

      def RemoverReparar(self,nodo):#Reparar árvore (manter as propriedades da árvore rubro-negra)
            while nodo != self._raiz and nodo.getCor() == 'preto':
                  if nodo == nodo.getPai().getFilhoEsq():
                        aux = nodo.getPai().getFilhoDir()
                  if aux.getCor() == 'vermelho':
                        aux.setCor("preto")
                        nodo.getPai().setCor('vermelho')
                        self.RotacaoEsq(nodo.getPai())
                        aux = nodo.getPai().getFilhoDir()
                  if aux.getFilhoEsq().getCor() == 'preto' and aux.getFilhoDir.getCor() == 'preto':
                        aux.setCor('vermelho')
                        nodo = nodo.getPai()
                  else:
                        if aux.getFilhoDir().getCor() == 'preto':
                              aux.getFilhoEsq().setCor('preto')
                              aux.setCor('vermelho')
                              self.RotacaoDir(aux)
                              aux = nodo.getPai().getFilhoDir()

      def BookCds(self, nodo):#Forma uma lista com os livros cadastrados (Método InOrder)
            if nodo != self._nil:
                  self.BookCds(nodo.getFilhoEsq())
                  self._lista.append('['+str(nodo.getDados().getCodigo())+']: '+nodo.getDados().getNome())
                  self.BookCds(nodo.getFilhoDir())

      def CpfCds(self,nodo):#Forma uma lista com os cpfs cadastrados (Método InOrder)
            if nodo != self._nil:
                  self.CpfCds(nodo.getFilhoEsq())
                  self._lista.append(nodo.getDados().getCPF())
                  self.CpfCds(nodo.getFilhoDir())       

      def PesquisarNodo(self, nome):#Pesquisando nodo(objeto) pelo nome
            aux = self._raiz
            if aux.getDados()==None:#Se raiz tiver os dados vazio, retorne o nil
                  return self._nil
            else:
                  if nome == None:
                          return self._nil
                  while aux.getDados().getNome() != nome: 
                      if aux.getDados().getNome() > nome:#Comparando o nome de entrada com o nome do nodo, caso seja maior aux recebe o seu filho esquerdo
                          aux = aux.getFilhoEsq()
                          if aux == self._nil:#Caso o filho esquerdo de aux for igual ao nó sentinela, retorne nil
                              return self._nil
                      else:#Caso contrário aux recebe seu filho Direiro
                          aux = aux.getFilhoDir()
                          if aux == self._nil:#Caso o filho direito de aux for igual ao nó sentinela, retorne nil
                              return self._nil
                  else:#Quando o nome do nodo for igual ao nome de busca, retorne o nodo encontrado
                         return aux
