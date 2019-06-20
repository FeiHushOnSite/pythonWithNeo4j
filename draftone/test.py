from py2neo import Node, Relationship, Graph

# persons = 'wang', 'zhao', 'ji'
# for person in persons:
#     node = Node("person", person)
#     print(node)
##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='jifeiyu')

knowledge = '1000603924', '1000612534', '1000612535', '1000612536', '1000612537', '1000612538', '1000630788'
knowledge1 = '1000612540', '1000612541', '1000612542', '1000612543', '1000612545'
knowledge2 = '1000612544'

type1 = '1000034606'
type2 = '1000034850'
type3 = '1000034849'

typepath = ['保险知识', '投保知识', '其他知识', '理赔知识']

node1 = Node('类目路径', name=typepath[0])
nodeTb = Node('类目路径', name=typepath[1])
nodeQt = Node('类目路径', name=typepath[2])
nodeLp = Node('类目路径', name=typepath[3])

graph.create(node1)
graph.create(nodeTb)
graph.create(nodeQt)
graph.create(nodeLp)

typepath_relation = Relationship(node1, '>>', nodeTb)
typepath_relation1 = Relationship(node1, '>>', nodeTb)
typepath_relation2 = Relationship(node1, '>>', nodeLp)
graph.create(typepath_relation)
graph.create(typepath_relation1)
graph.create(typepath_relation2)

for k in knowledge:
    node = Node('知识id', name=k)
    nodetype = Node('类目id', name=type1)
    r = Relationship(node, 'belong', node1)
    type_relation_path = Relationship(node1, 'belong', nodetype)
    graph.create(node)
    graph.create(nodetype)
    graph.create(r)
    graph.create(type_relation_path)

for k1 in knowledge1:
    node2 = Node('知识id', name=k1)
    nodetype1 = Node('类目id', name=type2)
    r1 = Relationship(node2, 'belong', nodeQt)
    type_relation_path1 = Relationship(nodeQt, 'belong', nodetype1)
    print(type_relation_path1)
    graph.create(node2)
    graph.create(nodetype1)
    graph.create(r1)
    graph.create(type_relation_path1)

node4 = Node('知识id', name=knowledge2)
nodetype3 = Node('类目id', name=type3)
r2 = Relationship(node4, 'belong', nodeLp)
type_relation_path12 = Relationship(nodeLp, 'belong', nodetype3)
print(type_relation_path12)
graph.create(node4)
graph.create(nodetype3)
graph.create(r2)
graph.create(type_relation_path12)

wordname = '投保流程', '运动', '意外险', '职业', '等待期', '婴儿', '区别'
wordname1 = '保单和发票', '买保险', '投保记录', '意外险', '客服热线'
wordname2 = '理赔,资料'

question = '投保流程', '运动险保障哪些活动', '一年期交通意外险和短期交通意外险有什么区别？', '意外险所有职业类别都承保吗', '意外险投保有等待期吗？', '刚出生的婴儿保吗？'

similarq = '怎么投保?想买保险要怎么操作', '运动险保障哪些活动'
similarqNode = Node('相关问题', name='怎么投保?想买保险要怎么操作')
similarqNode1 = Node('相关问题', name='运动险保障哪些活动')
graph.create(similarqNode)
graph.create(similarqNode1)

for w in wordname:
    nodew = Node('词条名称', name=w)
    rw = Relationship(nodew, 'belong', nodeTb)
    graph.create(nodew)
    graph.create(rw)
    for q in question:
        nodeqes = Node('关联问题', name=q)
        rq = Relationship(nodeqes, 'belong', nodew)
        question_relation_similarq = Relationship(similarqNode, 'belong', nodeqes)
        question_relation_similarq1 = Relationship(similarqNode1, 'belong', nodeqes)
        # print(question_relation_similarq,question_relation_similarq1)
        graph.create(nodeqes)
        graph.create(rq)
        graph.create(question_relation_similarq)
        graph.create(question_relation_similarq1)

question1 = '我如何获得保单和发票？', '一定要注册才可以买保险吗？', '投保完成后，我可以在哪里查到我的投保记录?', '我可以为朋友投保旅行险、健康险、意外险吗？'
similarq1 = '我要买保单'
similarq1Node = Node('相关问题', name=similarq1)
graph.create(similarq1Node)
Qt_Relation_Question = '我如何获得保单和发票', '一定要注册才可以买保险么?', '投保完成后,我可以在哪里查找到我的投保记录'
for w1 in wordname1:
    nodew1 = Node('词条名称', name=w1)
    rw1 = Relationship(nodew1, 'belong', nodeQt)
    graph.create(nodew1)
    graph.create(rw1)
    #  print(rw1)
    for qrq in Qt_Relation_Question:
        qrqNode = Node('关联问题', name=qrq)
        question_relation_similarq2 = Relationship(similarq1Node, 'belong', qrqNode)
        print(question_relation_similarq2)
        graph.create(qrqNode)
        graph.create(question_relation_similarq2)
