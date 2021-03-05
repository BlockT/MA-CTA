from src.graph import *
from src.agent import *
from src.subtask import *
from src.algorithm import *

# 初始化一个已有的分配方案，再利用此算法进行调整

# 1 先创建子任务,设置子任务的相互关联子任务
subtask1 = Subtask(1,(1,))
subtask2 = Subtask(2,(2,))
subtask3 = Subtask(3,(3,))
subtask4 = Subtask(4,(4,))

subtask1.setInDeTask((subtask2,subtask3))
subtask2.setInDeTask((subtask1,subtask3))
subtask3.setInDeTask((subtask1,subtask2))

# 2 再创建代理携带子任务，并设置代理的相互关联代理
agent1 = Agent(1,(subtask1,subtask2,subtask3))
agent2 = Agent(2,(subtask4,))
agent1.setInDeAgent()
agent2.setInDeAgent()

# 3 再将结点创建为图
g = Graph()

# vertext0 = g.addVertex(0,()) #元组内填入结点所拥有的能力
vertext1 = g.addVertex(1, (1, 2, 3))
vertext2 = g.addVertex(2, (1, 2, 3, 4))
# vertext3 = g.addVertex(3,())
# vertext4 = g.addVertex(4,())
# vertext5 = g.addVertex(5,())

g.addEdge(1, 2, 1)
g.addEdge(2, 1, 1)
# g.addEdge(0, 5, 2)
# g.addEdge(1, 2, 4)
# g.addEdge(2, 3, 9)
# g.addEdge(3, 4, 7)
# g.addEdge(3, 5, 3)
# g.addEdge(4, 0, 1)
# g.addEdge(5, 4, 8)
# g.addEdge(5, 2, 1)



#
# -------------------------------------------------
# 以下是测试数据.可删除
# -------------------------------------------------
#
print("-------------------Part of Initial Information-----------------------")
print(g.getVertices())

# vertList = { key :VertextObject}
# VertextObject =  ||key = key, connectedTo = {到达节点:权重}||   => |||| 表示的是权重的意思

# print(g)
i=0
for v in g:  # 循环类实例 => return ->  g = VertextObject的集合  v = VertextObject
    print(i)
    # print(v)
    i+=1
    for w in v.getConnections():  # 获得类实例的connectedTO
        # print(w)
        print("({},{},{}:{})".format(v.getId(), v.getCapabilities(), w.getId(), v.getWeight(w)))  ## 为什么会是这样 => 因为这个时候v就是class啊


# 4 再将代理选择一个结点进行排队
vertext2.addAgent(agent1)
vertext2.addAgent(agent2)

# print(vertext2)


print('\n-----------------before perform-------------------')
print([a.id for a in vertext1.agentList])
print([a.id for a in vertext2.agentList])

for v in g:
    allocation = Allocation(v,g)
    allocation.run()

print('\n-----------------perform result-------------------')
print([a.id for a in vertext1.agentList])
print([a.id for a in vertext2.agentList])

