from Classes.ServiceDAO import ServiceDAO

class Service:
    def __init__(self):
        pass

    def add_service(self):
        print "Cadastrar novo servico"
        service = ServiceDAO()
        service.getData()

