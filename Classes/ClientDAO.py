from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from Models.Model import Client as ClientModel

class ClientDAO:
    def __init__(self):
        pass

    def get(self,nome,cpf,segmento):
        try:
            engine = create_engine("postgresql://devops:4linux@127.0.0.1/dexter")
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            user = session.query(ClientModel).filter(ClientModel.name==nome, ClientModel.cpf==cpf, ClientModel.segment==segmento).first()
            cliSave = ClientModel(nome, cpf, segmento)
            session.add(cliSave)
            session.commit()
            print "Usuario %s adicionado com sucesso"%nome
        except Exception as e:
            session.rollback()

