from py2neo import Node, Relationship, Graph

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='jifeiyu')

typepath = ['保险知识', '投保知识', '其他知识', '理赔知识']

"""
相关index 静态变量
"""
index = '类目路径'
relation = 'belong'
entry = '词条名称'
relation_question = '关联问题'


# ------------------------------------------------------

def create_graph(nodeList):
    for node in nodeList:
        graph.create(node)
    return


nodeBx = Node(index, name=typepath[0])
nodeTb = Node(index, name=typepath[1])
nodeQt = Node(index, name=typepath[2])
nodeLp = Node(index, name=typepath[3])

node_typepath_list = nodeBx, nodeTb, nodeQt, nodeLp
create_graph(node_typepath_list)

nodeBx_relation_nodeTb = Relationship(nodeTb, relation, nodeBx)
nodeBx_relation_nodeQt = Relationship(nodeQt, relation, nodeBx)
nodeBx_relation_nodeLp = Relationship(nodeLp, relation, nodeBx)

node_relation_list = nodeBx_relation_nodeTb, nodeBx_relation_nodeQt, nodeBx_relation_nodeLp
create_graph(node_relation_list)

wordname = ['投保流程', '运动', '意外险', '婴儿', '区别']
wordname_nodeQt = ['保单和发票', '注册', '投保记录', '理赔,资料', '客服热线']

nodewordTb = Node(entry, name=wordname[0])
nodewordYd = Node(entry, name=wordname[1])
nodewordYwx = Node(entry, name=wordname[2])
nodewordYr = Node(entry, name=wordname[3])
nodewordQb = Node(entry, name=wordname[4])

nodeword_list =nodewordTb, nodewordYd, nodewordYwx, nodewordYr, nodewordQb
create_graph(nodeword_list)

nodewordBdFp = Node(entry, name=wordname_nodeQt[0])
nodewordRegister = Node(entry, name=wordname_nodeQt[1])
nodewordRecord = Node(entry, name=wordname_nodeQt[2])
nodewordResource = Node(entry, name=wordname_nodeQt[3])
nodewordCall = Node(entry, name=wordname_nodeQt[4])

graph.create(nodewordBdFp)
graph.create(nodewordRegister)
graph.create(nodewordRecord)
graph.create(nodewordResource)
graph.create(nodewordCall)

nodewordTb_relation_typepath = Relationship(nodewordTb, relation, nodeTb)
nodewordYd_relation_typepath = Relationship(nodewordYd, relation, nodeTb)
nodewordYwx_relation_typepath = Relationship(nodewordYwx, relation, nodeTb)
nodewordYr_relation_typepath = Relationship(nodewordYr, relation, nodeTb)

nodewordBdFp_relation_typepath = Relationship(nodewordBdFp, relation, nodeQt)
nodewordRegister_relation_typepath = Relationship(nodewordRegister, relation, nodeQt)
nodewordRecord_relation_typepath = Relationship(nodewordRecord, relation, nodeQt)
nodewordResource_relation_typepath = Relationship(nodewordResource, relation, nodeQt)
nodewordCall_relation_typepath = Relationship(nodewordCall, relation, nodeQt)

graph.create(nodewordTb_relation_typepath)
graph.create(nodewordYd_relation_typepath)
graph.create(nodewordYwx_relation_typepath)
graph.create(nodewordYr_relation_typepath)

graph.create(nodewordBdFp_relation_typepath)
graph.create(nodewordRegister_relation_typepath)
graph.create(nodewordRecord_relation_typepath)
graph.create(nodewordResource_relation_typepath)
graph.create(nodewordCall_relation_typepath)

# --------------------------------------------------------------------------------------
"""
投保流程
"""
question = Node(relation_question, name='投保流程')
graph.create(question)
relative_question = '怎么投保', '想买保险要怎么操作', '怎么购买保险?', '保单购买流程'
for rq in relative_question:
    rqNode = Node('相似问法', name=rq)
    relative_question_relation_question = Relationship(rqNode, relation, question)
    graph.create(rqNode)
    graph.create(relative_question_relation_question)

keyword = '投保', '买保险', '保单购买'
for k in keyword:
    nodeKeyWord = Node('关键词', name=k)
    nodeKeyWord_relation_relativequestion = Relationship(nodeKeyWord, relation, question)
    keyword_relation_wordname = Relationship(nodeKeyWord, relation, nodewordTb)
    graph.create(nodeKeyWord)
    graph.create(nodeKeyWord_relation_relativequestion)
    graph.create(keyword_relation_wordname)
# ----------------------------------------------------------------------------------------

"""
运动
"""
question1 = Node(relation_question, name='运动险保障哪些活动')
relative_question1 = Node('相似问法', name='运动险保障哪些活动')
question1_relation_relative_question1 = Relationship(question1, relation, relative_question1)
graph.create(question1)
graph.create(relative_question1)
graph.create(question1_relation_relative_question1)
keyword1 = '运动', '保障活动'
for k1 in keyword1:
    nodeKeyWord1 = Node('关键词', name=k1)
    keyword1_relation_wordname = Relationship(nodeKeyWord1, relation, nodewordYd)
    graph.create(nodeKeyWord1)
    graph.create(keyword1_relation_wordname)
"""
意外险
"""
question2 = Node(relation_question, name='一年期交通意外险和短期交通意外险有什么区别?')
question3 = Node(relation_question, name='意外险所有职业都承保么?')
question4 = Node(relation_question, name='意外险投保有等待期吗?')
question5 = Node(relation_question, name='我可以为朋友投保旅行险,健康险,意外险吗?')

question_list = question2, question3, question4, question5
create_graph(question_list)

keyword2 = '意外险', '一年交通意外', '短期交通意外', '区别'
keyword3 = '意外险', '职业类别', '投保'
keyword4 = '意外险', '等待期'
keyword5 = '意外险', '旅行险', '健康险', '投保', '买保险', '保单购买'

for k2 in keyword2:
    nodeKeyWord2 = Node('关键词', name=k2)
    keyword1_relation_wordname2 = Relationship(nodeKeyWord2, relation, nodewordYwx)
    keyword1_relation_question2 = Relationship(question2, relation, nodeKeyWord2)
    graph.create(nodeKeyWord2)
    graph.create(keyword1_relation_wordname2)
    graph.create(keyword1_relation_question2)

for k3 in keyword3:
    nodeKeyWord3 = Node('关键词', name=k3)
    keyword1_relation_wordname3 = Relationship(nodeKeyWord3, relation, nodewordYwx)
    keyword1_relation_question3 = Relationship(question3, relation, nodeKeyWord3)
    graph.create(nodeKeyWord3)
    graph.create(keyword1_relation_wordname3)
    graph.create(keyword1_relation_question3)

for k4 in keyword4:
    nodeKeyWord4 = Node('关键词', name=k4)
    keyword1_relation_wordname4 = Relationship(nodeKeyWord4, relation, nodewordYwx)
    keyword1_relation_question4 = Relationship(question4, relation, nodeKeyWord4)
    graph.create(nodeKeyWord4)
    graph.create(keyword1_relation_wordname4)
    graph.create(keyword1_relation_question4)

for k5 in keyword5:
    nodeKeyWord5 = Node('关键词', name=k5)
    keyword1_relation_wordname5 = Relationship(nodeKeyWord5, relation, nodewordYwx)
    keyword1_relation_question5 = Relationship(question5, relation, nodeKeyWord5)
    keyword1_relation_type = Relationship(nodeKeyWord5, relation, nodeQt)
    graph.create(nodeKeyWord5)
    graph.create(keyword1_relation_wordname5)
    graph.create(keyword1_relation_question5)

"""
婴儿
"""
question_baby = Node(relation_question, name='刚出生的婴儿保么?')
graph.create(question_baby)
keyword_baby = '婴儿', '投保'
for kb in keyword_baby:
    nodeKeyWord_baby = Node('关键词', name=kb)
    keywordbaby_relation_kb = Relationship(nodeKeyWord_baby, relation, nodewordYr)
    keywordbaby_relation_question = Relationship(question_baby, relation, nodeKeyWord_baby)
    graph.create(nodeKeyWord_baby)
    graph.create(keywordbaby_relation_kb)
    graph.create(keywordbaby_relation_question)
"""
保单和发票
"""
question_ticket = Node(relation_question, name='我如何获得保单和发票?')
graph.create(question_ticket)
keyword_ticket = '保单', '发票'
for kt in keyword_ticket:
    nodeKeyWord_ticket = Node('关键词', name=kt)
    keywordTicket_relation_ticket = Relationship(nodeKeyWord_ticket, relation, nodewordBdFp)
    keywordTicket_relation_question = Relationship(question_ticket, relation, nodeKeyWord_ticket)
    graph.create(nodeKeyWord_ticket)
    graph.create(keywordTicket_relation_ticket)
    graph.create(keywordTicket_relation_question)
"""
注册
"""
question_register = Node(relation_question, name='一定要注册才可以买保险吗?')
graph.create(question_register)
keyword_register = '注册', '投保', '买保险', '保单购买'
for kr in keyword_register:
    nodeKeyWord_register = Node('关键词', name=kr)
    keywordRegister_relation_register = Relationship(nodeKeyWord_register, relation, nodewordRegister)
    keywordRegister_relation_question = Relationship(question_register, relation, nodeKeyWord_register)
    graph.create(nodeKeyWord_register)
    graph.create(keywordRegister_relation_register)
    graph.create(keywordRegister_relation_question)
"""
投保记录
"""
question_record = Node(relation_question, name='投保完成后,我可以在哪里查到我的投保记录?')
graph.create(question_record)
keyword_record = '查询', '投保记录'
for krecord in keyword_record:
    nodeKeyword_record = Node('关键词', name=krecord)
    keywordrecord_relation_record = Relationship(nodeKeyword_record, relation, nodewordRecord)
    keywordrecord_relation_question = Relationship(question_record, relation, nodeKeyword_record)
    graph.create(nodeKeyword_record)
    graph.create(keywordrecord_relation_record)
    graph.create(keywordrecord_relation_question)

"""
客服热线
"""
question_call = Node(relation_question, name='客服热线')
question_call_relative = Node('相似问法', name='热线电话')
question_call_relative_question = Relationship(question_call_relative, relation, question_call)
question_call_relative_nodewordCall = Relationship(question_call, relation, nodewordCall)
graph.create(question_call)
graph.create(question_call_relative)
graph.create(question_call_relative_question)
graph.create(question_call_relative_nodewordCall)

"""
区别
"""
question_different = Node(relation_question, name='基本计划,标准计划和升级计划有什么区别?')
question_different_relative = Node('相似问法', name='三个计划的差别是什么?')
question_different_relative_question = Relationship(question_different_relative, relation, question_different)
question_call_relative_nodewordQb = Relationship(question_different, relation, nodewordQb)

graph.create(question_different)
graph.create(question_different_relative)
graph.create(question_different_relative_question)
graph.create(question_call_relative_nodewordQb)
