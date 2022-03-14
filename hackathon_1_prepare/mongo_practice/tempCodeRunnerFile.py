from pymongo import MongoClient
import pprint
client =MongoClient("mongodb://localhost:27017/")
db=client["myfirstdb"]
mycol=db["customers"]

