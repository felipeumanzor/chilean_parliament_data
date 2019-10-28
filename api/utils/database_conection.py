from pymongo import MongoClient, DESCENDING


def get_db():
    client = MongoClient()
    db = client.votoparlamentario
    return db