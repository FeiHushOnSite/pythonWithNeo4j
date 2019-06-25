from pymongo import MongoClient

import pandas as pd
client = MongoClient('mongodb://localhost:27017/')
db = client.test #指定数据库
collection = db.students  #指定集合
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
result = collection.insert_one(student)
print(result)
print(result.inserted_id)