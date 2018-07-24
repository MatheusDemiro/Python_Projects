class NohArvore:
    def __init__(self, idNoh, lista):
        self.idNoh = idNoh
        self.lista = lista
        
class ArvoreBinariaCheia(NohArvore):
    def __init__(self, h):
        self.h = h
        self.element = [None for x in range(2**(self.h)-1)]
        self.saida = []

    def adicionarNoh(self, nohDesejado):        
        self.nohDesejado = nohDesejado
        if self.element[0] == None:#Caso o nó raiz esteja vazio
            self.element[0] = nohDesejado
        else:
            nodo = self.element[0]
            indice = 0#Indice na lista
            while nodo != None:
                nodo = self.element[indice]
                if nodo == None:
                    self.element[indice] = nohDesejado
                    break
                elif nohDesejado.idNoh > nodo.idNoh:             
                    indice = 2*indice + 2#Filhos a direita
                else:
                    indice = 2*indice + 1#Filhos a esquerda
                    
    def pesquisarNoh(self,nohDesejado):
        nivel,indice,finish = 0,0,''
        nodo = self.element[indice].idNoh
        if nohDesejado == nodo:
             finish = '1'+' '+'0'#Caso o nohDesejado seja igual ao nó raiz
        else:#Caso o nohDesejado seja diferente do nó raiz
            while nodo != nohDesejado:
                if indice >= len(self.element):#Se nohDesejado ultrapassar a altura máxima da árvore
                    finish += '0'
                    break
                else:
                    nodo = self.element[indice]
                    if nohDesejado == nodo.idNoh:
                        finish+=str(nivel+1)+' '+str(indice)
                        break
                    elif nohDesejado > nodo.idNoh:
                        indice = 2*indice+2#Deslocando-se à direita
                        nivel+=1
                    else:
                        indice = 2*indice + 1#Deslocando-se à esquerda
                        nivel+=1
        self.saida.append(finish)       
            
entrada = input().split("!!!")
obj = ArvoreBinariaCheia(int(entrada[0]))
for i in entrada[1:]:
    objects = i.split()
    if len(objects) >= 2:#Caso a entrada seja composta por idNoh e lista
        idNoh = int(objects[0])
        lista = objects[1]
        obj.adicionarNoh(NohArvore(idNoh, lista))
    else:#Caso a entrada seja composta apenas pelo idNoh
        nohDesejado = int(objects[0])
        obj.pesquisarNoh(nohDesejado)
print("!!!".join(obj.saida))
