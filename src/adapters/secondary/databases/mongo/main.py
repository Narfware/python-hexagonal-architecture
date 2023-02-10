from pymongo import MongoClient


class Mongo_Client:
    def connect(self):
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = (
            "mongodb://mongoadmin:secret@mongo:27017/fast?authSource=admin"
        )

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONNECTION_STRING)

        return client
