from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from Models.Model import Product as ProductClass

class ProductDAO:
    def __init__(self):
        pass
    
    def get(self,nome,descricao,imagem):
        try:
            engine = create_engine("postgresql://devops:4linux@127.0.0.1/dexter")
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            prod = session.query(ProductClass).filter(ProductClass.name==nome, ProductClass.description==descricao, ProductClass.image==imagem).first()
            prodSave = ProductClass(nome, descricao, imagem)
            session.add(prodSave)
            session.commit()
            print "Container %s adicionado com sucesso"%nome
        except Exception as e:
            session.rollback()

