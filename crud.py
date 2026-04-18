from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from os import getenv

uri = f"mongodb+srv://{getenv('mongodb_username')}:{getenv('mongodb_password')}@{getenv('mongodb_uri')}"
client = MongoClient(uri, server_api=ServerApi('1'))


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)