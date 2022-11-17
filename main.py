import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:

    client = None

    def __init__(self, database_name= "db_name") -> None:

        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://<username>:<password>@cluster0.dtri5ce.mongodb.net/?retryWrites=true&w=majority"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name

        except Exception as e:
            raise e

if __name__ = '__main__':
  mongodb_client = MongoDBClient()
  print("collection name: ",mongodb_client.database.list_collection_names())
    
