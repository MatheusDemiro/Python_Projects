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
          position = self.func(int(noh.idNoh))
          if self.tam_tabela[position] is None:
               self.tam_tabela[position] = noh   
          else:
               tipe = str(type(self.tam_tabela[position])).split()
               if 'main' in tipe[1]:
                    self.tam_tabela[position] = [self.tam_tabela[position],noh]
               else:
                    self.tam_tabela[position].append(noh)              

     def Atualiza(self, noh):
          position = self.func(int(noh.idNoh))
          tipe = str(type(self.tam_tabela[position])).split()[1]
          if self.tam_tabela[position] is None:
            self.Insere(NoHash(noh.idNoh, noh.listaDados))
          elif 'main' in tipe:
               self.tam_tabela[position] = noh
          else:
               for objeto in self.tam_tabela[position]:
                    if objeto.idNoh == noh.idNoh:
                         indice = self.tam_tabela[position].index(objeto)
                         self.tam_tabela[position][indice] = noh

     def Pesquisa(self, noh):
          position = self.func(int(noh.idNoh))
          tipe = str(type(self.tam_tabela[position])).split()[1]
          if 'main' in tipe:
               saida.append(str(self.tam_tabela[position].getData()))
          else:
               for i in self.tam_tabela[position]:
                    if noh.idNoh == i.idNoh:
                         saida.append(str(i.getData()))

     def Excluir (self, noh):
          global saida
          position = self.func(int(noh.idNoh))
          tipe = str(type(self.tam_tabela[position])).split()[1]
          if 'main' in tipe:
                    self.tam_tabela[position] = None
          elif len(self.tam_tabela[position]) > 1:
               for element in self.tam_tabela[position]:
                         if element.idNoh == noh.idNoh:
                              aux = self.tam_tabela[position].index(element)
                              self.tam_tabela[position].remove(element)                         
          else:
               self.tam_tabela[position] =  None
obj = TabelaHash(funcaoHash)
entrada = input().split("!!!")
tam = len(entrada)
for i in range(len(entrada)):
          var = entrada[i].split(" ")
          if len(var) == 2:
               if var[0] == 'query':
                    obj.Pesquisa(NoHash(var[1],None))
               else:
                    obj.Excluir(NoHash(var[1],None))
          else:
               aux = var[2:]
               listaDados = eval(" ".join(aux))
               if var[0] == 'insert':
                    obj.Insere(NoHash(var[1], listaDados))
               if var[0] == 'update':
                    obj.Atualiza(NoHash(var[1], listaDados))
               if var[0] == 'delete':
                    obj.Excluir(NoHash(var[1], listaDados))     

print("!!!".join(saida))
