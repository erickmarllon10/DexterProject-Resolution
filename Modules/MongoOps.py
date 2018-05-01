from pymongo import MongoClient
class MongoOps:
    def __init__(self):
        self.client = MongoClient("127.0.0.1")
        self.db = self.client["dexter"]

    def getQueue(self,idService):
        return self.db.queue.find()

    def getServiceToInstall(self,idService):
        return self.db.queue.find({"_id":idService})

    def insertQueue(self,idService):
        self.db.queue.insert({"_id":idService,"status":0})

if __name__ == '__main__':
    m = MongoOps()
    m.insertQueue()
