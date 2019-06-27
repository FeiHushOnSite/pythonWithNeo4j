from py2neo import Node, Relationship, Graph

graph = Graph('http://localhost:7474', username='neo4j', password='jifeiyu')


def create_graph(nodeList):
    for node in nodeList:
        graph.create(node)
        return


index = "Claim_TYPE_NAME"
Claim_TYPE_NAME = "壽險死亡", "投資型死亡", "壽險殘廢", "醫療險", "重大疾（傷）病", "身故", "残疾", "医疗", "豁免保費"
index_node = Node(index, name="险种")
graph.create(index_node)
for ctn in Claim_TYPE_NAME:
    node = Node(index, name=ctn)
    graph.create(node)
    r = Relationship(node, "belong", index_node)
    graph.create(r)

index = "Insured_REAL_NAME"
Insured_REAL_NAME = "小冷", "较好的", "投保人A", "投保人B", "白敬亭", "张三", "理赔", "理赔啊理赔", "哇哇哇", "被保人A", "金金和阮阮", "理赔A", "躲藏", "理赔C", "周傑倫嘻嘻", "居一龙", "吴汉", "阿斯頓頂頂頂", "被保人B", "大大", "理赔B"

index_node = Node(index, name="投保人")
graph.create(index_node)
for irn in Insured_REAL_NAME:
    node = Node(index, name=irn)
    graph.create(node)

index = "SERVICE_NAME"
SERVICE_NAME = "VUL产品投入", "保单假期", "COI欠扣催告", "保单失效", "首期追加投资", "基金交易批处理", "VUL产品扣费", "理赔变更", "续期实收批处理", "保单借款", "保单借款还款", "保单自动贷款", "催告信件批处理", "保单失效", "個單保單借款還款", "自动失效批处理", "永久失效信件批处理", "个单生日性别更正", "保单贷款", "续期催告", "续期实收批处理", "個單復效"

index_node = Node(index, name="服务类型")

for sn in SERVICE_NAME:
    node = Node(index, name=sn)
    graph.create(node)

index = "RELA_ADDRESS"
RELA_ADDRESS = "臺北市士林區", "210", "110", "111", "201", "基隆市信義區"
index_node1 = Node(index, name="家庭住址")

for ra in RELA_ADDRESS:
    node = Node(index, name=ra)
    graph.create(node)

index = "CONCLUSION_DESC"
CONCLUSION_DESC = "給付", "拒賠", "赔付", "豁免保費"
index_node2 = Node(index, name="裁断结果")

for cd in CONCLUSION_DESC:
    node = Node(index, name=cd)
    graph.create(node)

index = "CLASS_3"
CLASS_3 = "食品商", "一般內勤人員", "製圖員", "內勤人員", "蛙人", "站長"
for c in CLASS_3:
    node = Node(index, name=c)
    graph.create(node)
