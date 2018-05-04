## The final 4Linux Project - DexterProject

#### My solution for DexterProject of Python Fundamentals Course - 4Linux.

#### Using the packages below:

* **Python version** = _2.7_
* **Models** = _Pymongo_, _SqlAlchemy_, _Datetime_, _paramiko_
* **Databases** = _Postgres_, _MongoDB_ 

#### Understanding the scenario:

Provision containers according to customer request. 
Both Clients and Products must be previously registered

#### To do before the steps below:
1.	Run 'python Models.py' at Models folder to create the database on Postgres
2.	Change values for "_self.servidor_, _username_ _and_ _password_" in SSOps.py conf in Modules Folder 
3.	Create a database in MongoDB and give a collection called '_queue_' with the dict {"_id":" ", "status":" "}. Ex: db.queue.insert({"id_": " ", "status": " "})
4.	Change Ip Address in MongoClient ("MongoDB IP") at MongoOps.py file 
5.	Make sure the host that you point in SSHOps.py has the docker service installed

#### 1.	How to register a customer?

First of all, for all services, run 'python AdmSSh.py' on project directory. So:

1.	Enter **1** to register a Client. Follow the steps and fill the blanks:
	* Set the name of the client
	* Set the CPF of the client (xxx.xxx.xxx-xx)
	* Set the team of the client (Ex: TI, RH, FIN, etc)

#### 2.	How to register a Product (Container)?

1.	Enter **2** to register a Product. Follow the steps and fill the blanks:
	* Set the name of the product
	* Set the Description of the product (Ex: xxx.xxx.xxx-xx)
	* Set the image of the container (Ex: Ubuntu:latest)
	
#### 3.	Register a Service: Applying Product (Container) to a Client

1.	Enter **3** to register a Product. Follow the steps and fill the blanks:
	* Chosse the ID of the Client
	* Chosse the ID of the Product
	* Set how long the client can access the container
	
#### 4.	verifying that the container was created
* Run "_docker ps_" at the docker host

