from Classes.ClientDAO import ClientDAO

class Client:
    def __init__(self,name="",cpf="",segment=""):
        self.id = 0
        self.name = name
        self.cpf = cpf
        self.segment = segment

    def add_client(self):
        print "Cadastro de Clientes"
        nameUser = raw_input("Digite o nome do Cliente: ")
        cpfUser = raw_input("Digite o cpf do cliente %s: "%nameUser)
        segmentUser = raw_input("Digite o segmento de mercado do cliente %s: "%nameUser)

        def __init__(self,nameUser,cpfUser,segmentUser):
            self.nameUser = nameUser
            self.cpfUser = cpfUser
            self.segmentUser = segmentUser

        try:
            cliDAO = ClientDAO()
            cliDAO.get(nameUser,cpfUser,segmentUser)
        except Exception as e:
            print "Erro: %s"%e

