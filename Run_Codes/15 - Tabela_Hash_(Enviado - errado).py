from funcHash import*
saida = []
class NoHash:
     """ Classe que define o nó e uma lista de dados"""
     def __init__(self, idNoh, listaDados):
          self.idNoh = idNoh
          self.listaDados = listaDados
     def getData(self):
          return self.listaDados

class TabelaHash (NoHash):

     def __init__(self, func):
          self.func = func
          tam_tabela = N
          self.tam_tabela = [None for x in range(tam_tabela+1)]
 
     def Insere(self, noh):
          position = self.func(int(noh.idNoh))#Chave = getData()
          if self.tam_tabela[position] is None:
               self.tam_tabela[position] = noh.getData()   
          else:
               if str(self.tam_tabela[position]).count(",") == 1:
                    self.tam_tabela[position] = [self.tam_tabela[position],noh.getData()]
               else:
                    dado = noh.getData()
                    self.tam_tabela[position].append(dado)
               

     def Atualiza(self, noh):
          position = self.func(int(noh.idNoh))
          if self.tam_tabela[position] is None:
            self.Insere(NoHash(noh.idNoh, noh.listaDados))
          elif str(self.tam_tabela[position]).count(",") == 1:
               self.tam_tabela[position] = noh.getData()
          else:
               for objeto in self.tam_tabela[position]:
                    if objeto[1] == noh.idNoh:
                         indice = self.tam_tabela[position].index(objeto)
                         self.tam_tabela[position][indice] = noh.getData()

     def Pesquisa(self, noh):
          return noh.getData()

     def Excluir (self, noh):
          global saida
          position = self.func(int(noh.idNoh))
          if str(self.tam_tabela[position]).count(",") == 1:
                    saida.append(str(self.tam_tabela[position]))
                    self.tam_tabela[position] = None
          else:
               for element in self.tam_tabela[position]:
                    if element[1] == int(noh.idNoh):
                         indice = self.tam_tabela[position].index(element)
                         saida.append(str(self.tam_tabela[position]))
                         self.tam_tabela[position].remove(element)
                         


            
obj = TabelaHash(funcaoHash)
entrada = input().split("!!!")
tam = len(entrada)
for i in range(len(entrada)):
          var = entrada[i].split(" ")
          OP = var[0]
          ID = var[1]

          if len(var) == 4:
               listaDados = eval(var[2]+var[3])

          elif len(var) == 2:
               pass           
          
          else:
               aux = var[2:]
               listaDados = eval(" ".join(aux))

          if OP == 'insert':
               obj.Insere(NoHash(ID, listaDados))
          if OP == "update":
               obj.Atualiza(NoHash(ID, listaDados))
          if OP == "query":
               obj.Excluir(NoHash(ID, listaDados))

print("!!!".join(saida))
