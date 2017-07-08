from django.db import models
import pymongo
# Create your models here.


def dbOperator(DBName,CName):

    client = pymongo.MongoClient("localhost",27017)

    db = client[DBName][CName]

    return db
