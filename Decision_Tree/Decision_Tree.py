from Tree import Tree
from TreeNode import TreeNode
#Esse algoritmo trata a apenas do arquivo de entrada descrito para o projeto (sem alterações).

doc_tree = open("text.txt","r+")
list_tree = doc_tree.readlines()#Lista com os elementos.
Tree_Decision = Tree()

def Format(node):#Função que formata a entrada.
      posI = node.index('a')
      if ':' in node:
            posF = node.index('(')-1
      else:
            posF = -1
      return node[posI:posF]

def Next(indice):#Função que retorna o próximo nodo.
      nodo = list_tree[indice+1]
      posI = nodo.index('a')
      return nodo[posI:]

guard = 0#Variável de auxílio
Tree_Decision.setRoot(TreeNode(list_tree[0].split()[0],list_tree[0].split()[1],list_tree[0].split()[2]))#Setando a raiz da árvore para o primeiro elemento do .txt.
for element in range(1,len(list_tree)):
      if element == guard:#Essa condição contribui para ignorar a linha seguinte. Caso o nodo que tenha '>=' não tenha ':', iremos selecionar próxima linha e igualar o element a guard para não tratarmos do mesmo nodo duas vezes.
            continue
      support = list_tree[element]
      node = Format(support)
      if '>=' not in node:
                  if ':' in node:
                        posF = node.index(':')
                        dados = node[0:posF-1].split()
                        folha = TreeNode(None, None, node.split()[4])#Nodo folha.
                        ref = Tree_Decision.LastNode()
                        dados = TreeNode(dados[0],dados[1],dados[2])#Pegando os objetos.
                        Tree_Decision.InsertNodeLeft(ref,dados)#Colocando o nodo à esquerda do último nodo inserido na árvore.
                        Tree_Decision.InsertNodeLeft(dados,folha)#Inserindo a folha à esquerda do nodo.
                  else:
                        node = TreeNode(node.split()[0],node.split()[1],node.split()[2])
                        ref = Tree_Decision.LastNode()#Selecionando o último elemento inserido na árvore.
                        Tree_Decision.InsertNodeLeft(ref,node)                        
      else:
                  posI = support.index('a')
                  if ':' in support:
                        posF = support.index("(")-1
                        nodo = support[posI:posF]
                        frag = Tree_Decision.SearchNode(nodo)#Realizando a pesquisa do nodo e o deletando da lista de objetos, logo, estamos construindo o seu lado direito.
                        folha = TreeNode(None,None,nodo.split()[4])
                        Tree_Decision.InsertNodeRight(frag, folha)
                  else:
                        assist = Format(support)
                        support = Next(element)
                        if ':' in support:#Caso a função Next retorne um elemento que tenha ':', em todos os casos que o elemento retornado tenha ':' em sua composição o sinal será de '<'.
                              frag = Tree_Decision.SearchNode(assist)#Realizando a busca do nodo que será o pai do nodo encontrado na variável support..
                              support = support[0:support.index('(')]
                              nodo = support[0:support.index(':')-1].split()
                              nodo = TreeNode(nodo[0], nodo[1], nodo[2])
                              folha = TreeNode(None, None, support[support.index(':')+1:-1])
                              Tree_Decision.InsertNodeRight(frag, nodo)#Setando o filho direito.
                              Tree_Decision.InsertNodeLeft(nodo, folha)#Setando a folha como filho esquerdo, pois o sinal de '<' está na composição do elemento retornado.
                              guard = element+1#Igualando a var guard a element para que o algoritmo desconsidere a próxima linha do txt, pois a mesma já foi selecionada.
                        else:
                              guard = element+1
                              posI = support.index('a')
                              nodo = support[posI:-1]
                              frag = Tree_Decision.SearchNode(node)
                              nodo = nodo.split()
                              nodo = TreeNode(nodo[0], nodo[1], nodo[2])
                              Tree_Decision.InsertNodeRight(frag, nodo)
doc_tree.close()
