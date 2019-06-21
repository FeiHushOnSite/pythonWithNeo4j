from pymongo import MongoClient
from py2neo import Node, Relationship, Graph

# import pandas as pd

client = MongoClient('mongodb://localhost:27017/')

db = client.test  # 指定数据库
collection_student = db.students  # 指定集合
collection_teacher = db.teachers
global info_id, info_name, info_age, info_gender, node
result = collection_teacher.find()
result_student = collection_student.find()

def create_node(list):
    for td in list:
        for tk in td.keys():
            if 'id' in tk:
                info_id = tk
            if 'name' in tk:
                info_name = tk
            if 'age' in tk:
                info_age = tk
            if 'gender' in tk:
                info_gender = tk
    node = Node(id=info_id, name=info_name, age=info_age, gender=info_gender)
    print(node)

create_node(result)



# node_teacher = Node(result)
# node_student = Node(result_student)
#
# relation = Relationship(node_student, 'teach', node_student)

# print(relation)

# teacher = Node(id='20170101', name='Jordan', age=20, gender='male')


result_teacher = collection_teacher.find()
print(result_student)
