from pymongo import MongoClient
from info import DATABASE_URI

db = MongoClient(DATABASE_URI)
bss = db["besetting"]
