from Classes.ProductDAO import ProductDAO

class Product:
    def __init__(self,name="",descricao="",imagem=""):
        self.id = 0
        self.name = name
        self.descricao = descricao
        self.imagem = imagem

    def add_product(self):
        print "Cadastro de produtos"
        nameProd = raw_input("Digite o nome do Container: ")
        desProd = raw_input("Digite a descricao do container %s: "%nameProd)
        imgProd = raw_input("Digite a imagem do container %s: "%nameProd)

        def __init__(self,nameProd,desProd,imgProd):
            self.nameProd = nameProd
            self.desProd = desProd
            self.imgProd = imgProd
        
        try:
            prodDAO = ProductDAO()
            prodDAO.get(nameProd,desProd,imgProd)
        except Exception as e:
            print "Erro: %s"%e

