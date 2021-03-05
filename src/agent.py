from src.subtask import *

class Agent():

    def __init__(self, key, carries):
        self.id = key            #代理名
        self.carries = carries   #因为此算法设计的一次调整过程中代理携带的任务也不变，所以用元组
        self.interDependAgent = []  # 存储对象
        self.belongToVer = None  # 代理所排队的结点
        self.setCarriesTaskBelong()

    def getId(self):
        return self.id

    def getCarries(self):
        return self.carries

    # 设置此代理所携带的子任务的所属代理，在计算开销的时候用
    def setCarriesTaskBelong(self):
        for subt in self.carries:
            subt.setBelongTo(self)

    # 设置此代理的相互依赖代理
    def setInDeAgent(self):
        for subt in self.carries:
            for interSubt in subt.interDependTask:
                # 不能重复添加相互依赖代理，类似集合
                if interSubt.belongToAgent not in self.interDependAgent:
                    self.interDependAgent.append(interSubt.belongToAgent)

    def getInDeAgent(self):
        return self.interDependAgent

    def setBelongToVer(self,belong):
        self.belongToVer = belong

    def getBelongTo(self):
        return self.belongToVer