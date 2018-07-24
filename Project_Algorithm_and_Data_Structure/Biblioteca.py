from Tree_Red_Black import Tree
from Node_Livros import NodeBook
from Node_Usuarios import NodeUser
from Node import Node
import pickle

def verificaCpf(arvoreUser, cpf):
      arvoreUser.CpfCds(arvoreUser.getRaiz())
      lista = arvoreUser.getLista()
      if cpf in lista:
                  return True
      else:
                  return False

def validaCpf(cpf):
      lista = []
      digitos = ''
      var1, var2 = 10,11
      for i in (cpf[0:9]):#primeiro dígito
            lista.append(int(i)*var1)
            var1-=1
      div = sum(lista)%11
      digito1 = 11 - div
      if digito1 > 9:
            valido = cpf[0:9]+'0'
      else:
            valido = cpf[0:9]+str(digito1)
      for i in (valido[0:10]):
            lista.append(int(i)*var2)
            var2-=1
      div = sum(lista[10:])%11
      digito2 = 11 - div
      if digito2 > 9:
            valido = cpf[0:10] + '0'
      else:
            valido = cpf[0:10] + str(digito2)
      if valido == cpf:
            return True
      else:
            return False


arvoreBook =Tree()#ÁRVORE COM LIVROS
arvoreUser =Tree()#ÁRVORE COM USUÁRIOS
while True:
      arvoreBook.BookCds(arvoreBook.getRaiz())
      code = len(arvoreBook.getLista())
      print("#===========================Bem-vindo===========================#")
      print("1-Cadastrar livros\n2-Cadastrar Usuários\n3-Solicitar Livro\n4-Devolução de livros\n5-Consulta de livro\n6-Remover livros\n7-Remover Usuários\n8-Carregar dados\n9-Salvar os dados cadastrados no sistema\n10-Mostrar livros disponíveis no acervo\n0-Sair do programa")
      escolha = input("Escolha uma das opções acima: ")
      if escolha == '1':
            nome = input("\nDigite o nome do livro: ").strip().lower()
            if nome == '':
                  print("\nNome inválido! Retorne ao menu principal e refaça a operação!\n")
                  continue
            code = id(code)
            nodo = NodeBook(nome,code,True)#True para livro disponível no acervo
            nodo = Node(nodo)
            arvoreBook.InserirNodo(nodo)
            print("\n|-|-|-Cadastro realizado com sucesso!-|-|-|\n\nDados:\n\tLivro cadastrado: %s\n\tCódigo                  : %s\n"%(nome.upper(),str(code)))
            code+=1
            continue

      if escolha == '2':
                        while True:
                              nome=input('\nDigite o nome do usuário: ').strip().lower()
                              cpf=input('Digite o CPF do usuário (apenas os números): ').strip()
                              if cpf == '' or cpf.isdigit() == False or nome == '':
                                 print("\nCPF ou Nome inválido!Informe apenas os números do cpf! Tente novamente!\n")
                                 continue
                              elif validaCpf(cpf) == False:
                                    print("\nCPF inválido! Refaça a operação e digite um cpf válido!\n")
                              elif verificaCpf(arvoreUser, str(cpf)) == False:#Verificando se o cpf está cadastrado ou não
                                    nodo = NodeUser(nome,cpf)
                                    nodo = Node(nodo)
                                    arvoreUser.InserirNodo(nodo)
                                    print("\nUsuário cadastrado com sucesso!\n")
                                    break
                              else:
                                          print("\nCPF já cadastrado no sistema! Tente novamente!\n")
                                          continue

      if escolha =='3':
            livro = input('\nInforme o nome do livro que desejas solicitar: ').strip().lower()
            pesquisaBook = arvoreBook.PesquisarNodo(livro).getDados()
            if pesquisaBook == None:
                  print("\nLivro não cadastrado no acervo!Retorne ao menu principal e tente um nome presente no acervo!\n")
                  continue
            if pesquisaBook.getStatus() == False:
                  print("\nLivro reservado!Tente outro livro!\n")
                  continue
            nome = input("\nDigite seu nome de usuário: ").strip().lower()
            cpf = input("Digite sua senha (apenas os números): ").strip()
            pesquisaUser = arvoreUser.PesquisarNodo(nome).getDados()
            if pesquisaUser == None:
                  print("\nUsuário não cadastrado! Retorne ao menu principal e faça o cadastro!\n")
                  continue
            elif pesquisaUser.getNome() == nome and pesquisaUser.getCPF() == cpf:#Dúvida aqui              
                        pesquisaBook.setStatus(False)#Atribuindo ao objeto nodo o status de False, ou seja, livro reservado
                        print("\nSolicitação realizada com sucesso!")
            else:
                  print("\nUsuário não econtrado! Usuário ou cpf incorreto. Tente novamente!\n")

      if escolha == '4':           
            nome = input('\nDigite o nome do livro que desejas devolver: ').strip().lower()
            nodo = arvoreBook.PesquisarNodo(nome).getDados()
            if nodo != None:
                  if nodo.getStatus() == False:
                        nodo.setStatus(True)
                        print("\nDevolução realizada com sucesso!")
                  else:
                        print("\nLivro não cadastrado!\n")

      if escolha =='5':
            nome = input ('\nDigite o nome do livro:').strip().lower()
            nodo = arvoreBook.PesquisarNodo(nome).getDados()
            if nodo.getStatus() == False:
                  print ("\nLivro não disponível na biblioteca!\n")
                  continue
            else:
                  print ("\nNome do Livro: %s\nCódigo: %s\n"%(nodo.getNome().upper(), str(nodo.getCodigo())))

      if escolha=='6':
          nome=input("\nDigite o nome do livro: ").strip().lower()
          nodo=arvoreBook.PesquisarNodo(nome)
          if nodo.getDados()!=None:
              arvoreBook.RemoverNodo(nodo)
              print('\nLivro Removido com sucesso!')
          else:
              print("\nLivro não encontrado!")

      if escolha=='7':#Remover usuário
            cpf = input("\nInforme número do cpf (apenas os números): ")
            if verificaCpf(arvoreUser, cpf):                  
                  nome = input("Digite o nome do usuário: ").strip().lower()
                  nodo = arvoreUser.PesquisarNodo(nome)
                  if nodo.getDados()!=None and nodo.getDados().getCPF() == cpf:
                        arvoreUser.RemoverNodo(nodo)
                        print('\nUsuário Removido com sucesso!')
                  else:
                        print("\nNome ou CPF não encontrados na base dados!Retorne ao menu principal e refaça a operação!\n")
            else:
                  print("\nUsuário não encontrado na base de dados! Tente novamente com dados válidos!\n")

      if escolha == '8':#Carregar árvore de dados
            while True:#Só vai sair do loop se forem digitados nomes válidos
                  try:
                        Book = input("\nDigite nome do arquivo que contem os livros cadastrados: ").strip()
                        User = input("Digite nome do arquivo que contem os usuários cadastrados: ").strip()
                        arquivoB = open(Book,'rb')
                        arquivoU = open(User,'rb')
                        arvoreBook = pickle.load(arquivoB)#Carregando árvore de livros
                        arvoreUser = pickle.load(arquivoU)#Carregando árvore de usuários
                        print("\n##Dados carregados com sucesso!##\n")
                        break
                  except FileNotFoundError:
                        print("\nArquivo(s) não encontrado(s)!!")
                        
      if escolha=='9':#Salvar árvore de dados
            Book = input("\nInforme o nome para o arquivo de armazenamento dos Livros: ").strip()
            User = input("Informe o nome para o arquivo de armazenamento dos Usuários: ").strip()
            arqBook = open(Book,'wb')
            arqUser = open(User, 'wb')
            pickle.dump(arvoreBook, arqBook)
            pickle.dump(arvoreUser, arqUser)
            arqBook.close()
            arqUser.close()
            print("\n##Os dados foram salvos com sucesso!##\n")
            continue

      if escolha == '10':
            livros = arvoreBook.BookCds(arvoreBook.getRaiz())
            acervo = arvoreBook.getLista()
            print("\nLivros disponíveis no acervo:\n")
            for i in acervo:
                  print(i.upper())
            continue
      
      if escolha == '0':
            print("\nPrograma encerrado com sucesso!\n")
            break
      
      if escolha == '' or escolha not in ['1','2','3','4','5','6','7','8','9','10']:
            print('\nDigite uma opção válida!\n')
            continue
