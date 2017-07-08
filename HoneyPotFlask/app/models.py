import pymongo


def dbOperator(DBName,CName):

    client = pymongo.MongoClient("localhost",27017)

    db = client[DBName][CName]

    return db
