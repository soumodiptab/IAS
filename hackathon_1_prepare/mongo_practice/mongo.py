from pymongo import MongoClient
import pprint
client =MongoClient("mongodb://localhost:27017/")
db=client["myfirstdb"]
collection = db["test"]

post1= {"id":5,"name":"joe"}
post2={"id":6,"name":"bill"}
collection.insert_one(post1)
results=collection.find()
for result in results:
    print(result)
