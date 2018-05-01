from Modules.SSHOps import SSHOps

class DockerOps:
    def createContainer(self,id,image,name):
        command = "docker run -d -ti --name %s %s /bin/bash"%("%s_%s_%s"%(image,id,name),"webservercloud")
        ssh = SSHOps()
        res = ssh.executarComandoRemoto(command)
        if res['status'] == 1:
            print res['message']
