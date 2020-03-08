import pymongo
from config import Config

class MongoConn:
    def __init__(self):
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        myclient = pymongo.MongoClient(Config.MongoDBConnectString)
        mydb = myclient["pytestdb"]
        self.mycol = mydb["movies"]
