from pymongo import MongoClient
import os

# set up MongoDB connection
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

# Use database "mydb"
db = client.mydb

# Use collection "checkpoints" in the database
collection = db.lists

def insert_brevet(brevet_dist, start_time, controls):
    #db.insert_one
    
    output = collection.insert_one({
        "brevet_dist": brevet_dist,
        "start_time": start_time,
        "controls": controls
    })

    _id = output.inserted_id

    return str(_id)

def get_brevet():
    # db.find_one
    """
    Obtains the newest document in the "lists" collection in database "mydb".
    Returns brevet_dist, start_time, controls as a tuple.
    """

    lists = collection.find().sort("_id", -1).limit(1)

    for list in lists:
        return list["brevet_dist"], list["start_time"], list["controls"]
