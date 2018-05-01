from Classes.Client import Client
from Classes.Product import Product
from Classes.Service import Service

def menu():
    print "\
            1 - Cadastrar cliente: \n\
            2 - Cadastrar Produto: \n\
            3 - Cadastrar Servico: "

    opcao = input("Digite a sua opcao: ")
    return opcao

def switch(x):
    cli = Client()
    prod = Product()
    serv = Service()
    dict_options = {1:cli.add_client,
                    2:prod.add_product,
                    3:serv.add_service}
    dict_options[x]()

if __name__ == '__main__':
    try:
        while True:
            switch(menu())
    except Exception as e:
        print "Erro: %s"%e
