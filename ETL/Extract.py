import pymongo


def extract_mongo_data():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.Food
    collection = db.Restaurants
    cursor = collection.find({})
    data = list(cursor)
    return data
