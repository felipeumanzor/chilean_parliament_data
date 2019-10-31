from pymongo import MongoClient, DESCENDING


def get_db():
    client = MongoClient(username="vp2", password='2-X(mVeww:Hk"V9R', authSource='votoparlamentario')
    db = client.votoparlamentario
    return db
