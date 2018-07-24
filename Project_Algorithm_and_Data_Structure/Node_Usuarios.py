#Classe de contrução do usuário
#Dados: Nome, CPF, Data_de_nascimento
class NodeUser:
      def __init__(self, Nome, CPF):
            """Preencha os campos Nome e CPF, respectivamente."""
            self._nome = Nome
            self._cpf = CPF

      def getNome(self):
            return self._nome

      def getCPF(self):
            return self._cpf
