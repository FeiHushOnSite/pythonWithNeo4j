from py2neo import Node, Relationship, Graph

from py2neo import Node, Relationship, Graph

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='jifeiyu')

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

global info_id, info_name, info_age, info_gender, node

for td in test_data:
    print(td.keys())
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
print('result:' + info_id, ':' , info_name, ':',info_age, ':',info_gender)
print(node)
graph.create(node)