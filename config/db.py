from pymongo import MongoClient

conn = MongoClient("mongodb://user123:user123@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")


