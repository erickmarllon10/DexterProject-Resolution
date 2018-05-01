from Classes.Client import Client as ClientClass
from Classes.Product import Product as ProductClass
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from Models.Model import Client
from Models.Model import Product
from Models.Model import Service
from datetime import datetime,timedelta
from Modules.MongoOps import MongoOps
from Modules.DockerOps import DockerOps

class ServiceDAO:
    def __init__(self,service=""):
        self.service = service

    def getData(self):
        try:
            engine = create_engine("postgresql://devops:4linux@127.0.0.1/dexter")
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
        
            # Clients Search
            cli = session.query(Client).all()
            for clients in cli:
                print "Id:",clients.id, "-", "Nome:",clients.name 
            ClientID = input("Escolha o ID do cliente: ")

            # Add Service
            prod = session.query(Product).all()
            for products in prod:
                print "Id:",products.id, "-", "Nome:",products.name, "-", "Descricao: ",products.description
            productID = input("Digite o ID do produto para o cliente selecionado: ")

            print "Data de compra do servico: ",datetime.now()
            dateBuy = datetime.now()
            finalDate = input("Informe quantos dias o cliente tera acesso a esse servico: Ex:(1,2,3...): ")
            print "Acesso liberado ate a data: ",dateBuy + timedelta(finalDate)
            finalBuy = dateBuy + timedelta(finalDate)

            # Persisting Service in Oracle Databse
            saveData = Service(dateBuy, finalBuy, ClientID, productID)
            session.add(saveData)
            session.commit()
            print "Servico registrado com sucesso."
            serviceID = session.query(Service).filter(Service.request_date==dateBuy, 
                            Service.cancel_date==finalBuy, 
                                Service.client_id==ClientID, 
                                    Service.product_id==productID).first()

            print "O ID do servico e: %s"%serviceID.id

            # Putting ID Service to MongoDB Collection
            mongo = MongoOps()
            mongo.insertQueue(serviceID.id)
            mongo.getServiceToInstall(serviceID.id)
            print "Existem %s servicos na fila"%(mongo.getQueue(serviceID.id).count())

            # Validating Service
            service = session.query(Service,Client,Product).join(Client,Product).filter(Service.id==serviceID.id).first()
            if service is None:
                return None

            # Display Service to install
            for serviceMongo in mongo.getServiceToInstall(serviceID.id):
                print serviceMongo

            # Display information about the current install Service
            print "ID: %s Data de Contratacao: %s"%(serviceID.id,service.Service.request_date)
            print "Instalando o servico para o cliente; %s"%service.Client.name
            print "Servico a ser instalado: %s"%service.Product.name

            # Creating Containers in Docker for the Service
            docker = DockerOps()
            res = docker.createContainer(serviceID.id, service.Product.image, service.Product.name)

        except Exception as e:
            print "Algum erro aconteceu %s"%e

