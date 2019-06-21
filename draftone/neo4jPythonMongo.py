from pymongo import MongoClient
from py2neo import Node, Relationship, Graph
#import pandas as pd

client = MongoClient('mongodb://localhost:27017/')


def create_node(list):
    for node in list:
        for parm in node.keys():
            keys = node.keys
            if 'id' in keys:
                id = parm['id']
        # if 'name' in keys:
        #     name = node.values()
        # if 'age' in keys:
        #     age = node.values()
        # if 'gender' in keys:
        #     gender = node.keys()
        # node = Node(id=id, name=name, age=age, gender=gender)
        # print(id)
            print(id)
            return


db = client.test  # 指定数据库
collection_student = db.students  # 指定集合
collection_teacher = db.teachers

result = collection_teacher.find_one()
result_student = collection_student.find()

# node_teacher = Node(result)
# node_student = Node(result_student)
#
# relation = Relationship(node_student, 'teach', node_student)

# print(relation)

#teacher = Node(id='20170101', name='Jordan', age=20, gender='male')

test_data = {'id': '20170101',
             'name': 'Jordan',
             'age': 20,
             'gender': 'male'}, {'id': '20170101',
                                 'name': 'Jordan',
                                 'age': 20,
                                 'gender': 'male'}, {'id': '20170101',
                                                     'name': 'Jordan',
                                                     'age': 20,
                                                     'gender': 'male'}
print(create_node(test_data))
# insert_data = collection_teacher.insert(test_data)
# print(insert_data)

# print(teacher)
# print(result)
# print(result_student)

result_teacher = collection_teacher.find()
print(result_student)