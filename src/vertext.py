from src.agent import *

class Vertext():  # 包含了顶点信息,以及顶点连接边

    def __init__(self, key, capablities):  # key表示是添加的顶点
        self.id = key
        self.capabilities = capablities  #初始化结点具有的能力,因为结点能力不需要变化，所以此处我们可以使用元组
        self.connectedTo = {}   # 初始化临接列表
        self.agentList = {}     # 初始化代理队列，因为算法调整后，代理会移动，所以此处不能用元组；
                                # 而且因为在组队的时候涉及到此代理在此结点已加入候补处理队伍（即看他
                                # 是否能够组队移动）的标记位，所以用字典，键是代理名，值是标记位

    def addNeighbor(self, nbr, weight=0):  # 这个是赋值权重的函数
        self.connectedTo[nbr] = weight

    def addAgent(self, agent, f=0):
        self.agentList[agent] = f
        agent.setBelongToVer(self)   # 此处传的是结点对象本身，不像subtask传的是id，因为后面要用到对象获取权重，字典的key是结点对象
                                     # 子任务也要传对象本身，id不行
    def delAgent(self, agent):
        self.agentList.pop(agent)

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo]) \
               + ' own_Capablities: ' + str(self.capabilities) + ' agentList: ' + str([x.id for x in self.agentList])

    def getConnections(self):  # 得到这个顶点所连接的其他的所有的顶点 (keys类型是class)
        return self.connectedTo.keys()

    def getId(self):  # 返回自己的key
        return self.id

    def getWeight(self, nbr):  # 返回所连接ner顶点的权重是多少
        return self.connectedTo[nbr]

    def getCapabilities(self):
        return self.capabilities


