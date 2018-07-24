#Projeto Árvore-Decisão.py
#By: Matheus Paulo e Lucas Marsol

from Tree_Decision import Tree_Decision

# NAVEGANDO PELA ÁRVORE DE ACORDO COM AS ENTRADAS DO USUÁRIO
aux=Tree_Decision.getRoot()
while aux.getTextNode()!=None:
            print("\n=============================")
            print('\t',aux.getTextNode(),aux.getSignNode(),aux.getIdNode())
            print("=============================\n")
            resposta=input('Digite sua resposta(0 ou 1): ')#Entrada binária: 1 para verdadeiro e 0 para falso
            if resposta == '0':#Caminhar para a esquerda
                  aux=aux.getSonLeft()
            elif resposta== '1':#Caminhar para a direita
                  aux=aux.getSonRight()
            else:
                  print("Entrada inválida,tente novamente.")
print('---------------------------\n')
print("Resultado:",aux.getIdNode()+'\n')
print('---------------------------\n')

