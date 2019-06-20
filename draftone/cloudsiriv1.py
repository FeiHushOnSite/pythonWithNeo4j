from py2neo import Node, Relationship, Graph

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='jifeiyu')

typepath = ['保险知识', '投保知识', '其他知识', '理赔知识']

nodeBx = Node('类目路径', name=typepath[0])
nodeTb = Node('类目路径', name=typepath[1])
nodeQt = Node('类目路径', name=typepath[2])
nodeLp = Node('类目路径', name=typepath[3])

graph.create(nodeBx)
graph.create(nodeTb)
graph.create(nodeQt)
graph.create(nodeLp)

nodeBx_relation_nodeTb = Relationship(nodeTb, 'belong', nodeBx)
nodeBx_relation_nodeQt = Relationship(nodeQt, 'belong', nodeBx)
nodeBx_relation_nodeLp = Relationship(nodeLp, 'belong', nodeBx)

graph.create(nodeBx_relation_nodeTb)
graph.create(nodeBx_relation_nodeQt)
graph.create(nodeBx_relation_nodeLp)

wordname = ['投保流程', '运动', '意外险', '婴儿']
wordname_nodeQt = ['保单和发票', '注册', '投保记录', '理赔,资料', '客服热线']

nodewordTb = Node('词条名称', name=wordname[0])
nodewordYd = Node('词条名称', name=wordname[1])
nodewordYwx = Node('词条名称', name=wordname[2])
nodewordYr = Node('词条名称', name=wordname[3])

graph.create(nodewordTb)
graph.create(nodewordYd)
graph.create(nodewordYwx)
graph.create(nodewordYr)

nodewordBdFp = Node('词条名称', name=wordname_nodeQt[0])
nodewordRegister = Node('词条名称', name=wordname_nodeQt[1])
nodewordRecord = Node('词条名称', name=wordname_nodeQt[2])
nodewordResource = Node('词条名称', name=wordname_nodeQt[3])
nodewordCall = Node('词条名称', name=wordname_nodeQt[4])

graph.create(nodewordBdFp)
graph.create(nodewordRegister)
graph.create(nodewordRecord)
graph.create(nodewordResource)
graph.create(nodewordCall)

nodewordTb_relation_typepath = Relationship(nodewordTb, 'belong', nodeTb)
nodewordYd_relation_typepath = Relationship(nodewordYd, 'belong', nodeTb)
nodewordYwx_relation_typepath = Relationship(nodewordYwx, 'belong', nodeTb)
nodewordYr_relation_typepath = Relationship(nodewordYr, 'belong', nodeTb)

nodewordBdFp_relation_typepath = Relationship(nodewordBdFp, 'belong', nodeQt)
nodewordRegister_relation_typepath = Relationship(nodewordRegister, 'belong', nodeQt)
nodewordRecord_relation_typepath = Relationship(nodewordRecord, 'belong', nodeQt)
nodewordResource_relation_typepath = Relationship(nodewordResource, 'belong', nodeQt)
nodewordCall_relation_typepath = Relationship(nodewordCall, 'belong', nodeQt)

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
question = Node('关联问题', name='投保流程')
graph.create(question)
relative_question = '怎么投保', '想买保险要怎么操作', '怎么购买保险?', '保单购买流程'
for rq in relative_question:
    rqNode = Node('相似问法', name=rq)
    relative_question_relation_question = Relationship(rqNode, 'belong', question)
    graph.create(rqNode)
    graph.create(relative_question_relation_question)

keyword = '投保', '买保险', '保单购买'
for k in keyword:
    nodeKeyWord = Node('关键词', name=k)
    nodeKeyWord_relation_relativequestion = Relationship(nodeKeyWord, 'belong', question)
    keyword_relation_wordname = Relationship(nodeKeyWord, 'belong', nodewordTb)
    graph.create(nodeKeyWord)
    graph.create(nodeKeyWord_relation_relativequestion)
    graph.create(keyword_relation_wordname)
# ----------------------------------------------------------------------------------------

"""
运动
"""
question1 = Node('关联问题', name='运动险保障哪些活动')
relative_question1 = Node('相似问法', name='运动险保障哪些活动')
question1_relation_relative_question1 = Relationship(question1, 'belong', relative_question1)
graph.create(question1)
graph.create(relative_question1)
graph.create(question1_relation_relative_question1)
keyword1 = '运动', '保障活动'
for k1 in keyword1:
    nodeKeyWord1 = Node('关键词', name=k1)
    keyword1_relation_wordname = Relationship(nodeKeyWord1, 'belong', nodewordYd)
    graph.create(nodeKeyWord1)
    graph.create(keyword1_relation_wordname)
"""
意外险
"""
question2 = Node('关联问题', name='一年期交通意外险和短期交通意外险有什么区别?')
question3 = Node('关联问题', name='意外险所有职业都承保么?')
question4 = Node('关联问题', name='意外险投保有等待期吗?')
question5 = Node('关联问题', name='我可以为朋友投保旅行险,健康险,意外险吗?')
graph.create(question2)
graph.create(question3)
graph.create(question4)
graph.create(question5)

keyword2 = '意外险', '一年交通意外', '短期交通意外', '区别'
keyword3 = '意外险', '职业类别', '投保'
keyword4 = '意外险', '等待期'
keyword5 = '意外险', '旅行险', '健康险', '投保', '买保险', '保单购买'

for k2 in keyword2:
    nodeKeyWord2 = Node('关键词', name=k2)
    keyword1_relation_wordname2 = Relationship(nodeKeyWord2, 'belong', nodewordYwx)
    keyword1_relation_question2 = Relationship(question2, 'belong', nodeKeyWord2)
    graph.create(nodeKeyWord2)
    graph.create(keyword1_relation_wordname2)
    graph.create(keyword1_relation_question2)

for k3 in keyword3:
    nodeKeyWord3 = Node('关键词', name=k3)
    keyword1_relation_wordname3 = Relationship(nodeKeyWord3, 'belong', nodewordYwx)
    keyword1_relation_question3 = Relationship(question3, 'belong', nodeKeyWord3)
    graph.create(nodeKeyWord3)
    graph.create(keyword1_relation_wordname3)
    graph.create(keyword1_relation_question3)

for k4 in keyword4:
    nodeKeyWord4 = Node('关键词', name=k4)
    keyword1_relation_wordname4 = Relationship(nodeKeyWord4, 'belong', nodewordYwx)
    keyword1_relation_question4 = Relationship(question4, 'belong', nodeKeyWord4)
    graph.create(nodeKeyWord4)
    graph.create(keyword1_relation_wordname4)
    graph.create(keyword1_relation_question4)

for k5 in keyword5:
    nodeKeyWord5 = Node('关键词', name=k5)
    keyword1_relation_wordname5 = Relationship(nodeKeyWord5, 'belong', nodewordYwx)
    keyword1_relation_question5 = Relationship(question5, 'belong', nodeKeyWord5)
    keyword1_relation_type = Relationship(nodeKeyWord5, 'belong', nodeQt)
    graph.create(nodeKeyWord5)
    graph.create(keyword1_relation_wordname5)
    graph.create(keyword1_relation_question5)

"""
婴儿
"""
question_baby = Node('关联问题', name='刚出生的婴儿保么?')
graph.create(question_baby)
keyword_baby = '婴儿', '投保'
for kb in keyword_baby:
    nodeKeyWord_baby = Node('关键词', name=kb)
    keywordbaby_relation_kb = Relationship(nodeKeyWord_baby, 'belong', nodewordYr)
    keywordbaby_relation_question = Relationship(question_baby, 'belong', nodeKeyWord_baby)
    graph.create(nodeKeyWord_baby)
    graph.create(keywordbaby_relation_kb)
    graph.create(keywordbaby_relation_question)
"""
保单和发票
"""
question_ticket = Node('关联问题', name='我如何获得保单和发票?')
graph.create(question_ticket)
keyword_ticket = '保单', '发票'
for kt in keyword_ticket:
    nodeKeyWord_ticket = Node('关键词', name=kt)
    keywordTicket_relation_ticket = Relationship(nodeKeyWord_ticket, 'belong', nodewordBdFp)
    keywordTicket_relation_question = Relationship(question_ticket, 'belong', nodeKeyWord_ticket)
    graph.create(nodeKeyWord_ticket)
    graph.create(keywordTicket_relation_ticket)
    graph.create(keywordTicket_relation_question)
"""
注册
"""
question_register = Node('关联问题', name='一定要注册才可以买保险吗?')
graph.create(question_register)
keyword_register = '注册', '投保', '买保险', '保单购买'
for kr in keyword_register:
    nodeKeyWord_register = Node('关键词', name=kr)
    keywordRegister_relation_register = Relationship(nodeKeyWord_register, 'belong', nodewordRegister)
    keywordRegister_relation_question = Relationship(question_register, 'belong', nodeKeyWord_register)
    graph.create(nodeKeyWord_register)
    graph.create(keywordRegister_relation_register)
    graph.create(keywordRegister_relation_question)
"""
投保记录
"""
question_record = Node('关联问题', name='投保完成后,我可以在哪里查到我的投保记录?')
graph.create(question_record)
keyword_record = '查询', '投保记录'
for krecord in keyword_record:
    nodeKeyword_record = Node('关键词', name=krecord)
    keywordrecord_relation_record = Relationship(nodeKeyword_record, 'belong', nodewordRecord)
    keywordrecord_relation_question = Relationship(question_record, 'belong', nodeKeyword_record)
    graph.create(nodeKeyword_record)
    graph.create(keywordrecord_relation_record)
    graph.create(keywordrecord_relation_question)

"""
客服热线
"""
question_call = Node('关联问题', name='客服热线')
question_call_relative = Node('相似问法', name='热线电话')
graph.create(question_call)
graph.create(question_call_relative)

