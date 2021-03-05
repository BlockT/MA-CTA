class Allocation():

    # 在每个结点上调用此算法，在算法内遍历整个结点内所有代理，所以只需要初始化此算法针对哪个结点进行处理即可
    def __init__(self, currentVertext,currentGraph):
        self.currentVertext=currentVertext
        self.g=currentGraph

        # self.coopTeam_G = {}    # 需要组成的 合作转移team  G
        # self.max = 0;

    def run(self):
        # print(self.currentVertext.agentList.values()) # 代理在结点初始flag都是0
        tmp_currentAgentlist = self.currentVertext.agentList.copy()
        for a in tmp_currentAgentlist:
            # 每个代理都可能有一个新的协作队伍，所以都要重新初始化
            coopTeam_G=[]      # 初始化空列表装载协作队伍成员结点对象
            maxBenefit=0       # 迁移的最大收益
            targetVer=None     # 目标结点，初始为空
            queueDealTeam=[a]  # 候补处理的代理序列，装载代理对象，初始将当前代理作为基代理存入，以通过
                               # 如下算法在节点内广度遍历与其相互依赖的其他代理，添加到queue中等待处理
            self.currentVertext.agentList[a]=1  # 将代理a在此结点的f标志位设为1，代表其已加入处理队伍

            while len(queueDealTeam)>0:
                lG=len(coopTeam_G)      # 后面计算waitCost的时候用
                ax=queueDealTeam.pop(0)  # 从列表头部弹出，因为后面append添加的代理是在尾部添加，
                                         # 需要符合广度遍历原则，算法原则是a的IA=a1，a2，
                                         # a2还未弹出时处理a1后添加a1的IA=a11,a12,再处理a2添加a2的IA=a21,a22
                tag=False
                for v in self.g:
                    if v.id != self.currentVertext.id:
                        benefit = self.cacuBenefit(self.currentVertext, v, lG, coopTeam_G)
                        shouldMove = True
                        if benefit > maxBenefit:
                            tmpG = coopTeam_G[:]
                            tmpG.append(ax)
                            for a in tmpG:
                                for subt in a.carries:
                                    for reqCap in subt.req_capab:
                                        if reqCap not in v.capabilities:
                                            shouldMove = False
                        else:
                            shouldMove =False
                        if shouldMove == True:
                            tag = True
                            maxBenefit = benefit
                            targetVer = v
                if tag == True:
                    coopTeam_G.append(ax)
                    for ay in ax.interDependAgent:
                        if ay.belongToVer.id == self.currentVertext.id and ay.belongToVer.agentList[ay]!=1:
                            queueDealTeam.append(ay)
                            ay.belongToVer.agentList[ay] = 1
            if len(coopTeam_G) > 0:
                self.moveGtoTarget(coopTeam_G, targetVer)


    def cacuBenefit(self, nx, ny, lG, G):
        benefit = self.cacuExcCost(nx, lG, G) - self.cacuExcCost(ny, lG, G)
        return benefit

    def cacuExcCost(self, vertex, lG, G):
        m = 3
        n = 5
        excCost = m * self.cacuWaitCost(vertex, lG) + n * self.cacuCommCost(vertex, G)
        return excCost

    def cacuWaitCost(self, vertext, lG):
        waitCost = 0
        # lG+1是因为算的是G U ax，若是本地结点，len(vertext.agentList)就包含有G and ax
        if vertext.id == self.currentVertext.id:
            l_ver = len(vertext.agentList)
        else :
            l_ver=len(vertext.agentList) + (lG + 1)
        waitCost = ((lG+1) * ((l_ver - (lG + 1) + 1) + l_ver))/2  # 等差数列求和公式
        return waitCost

    def cacuCommCost(self,vertext, G):
        commCost = 0
        for a in G:
            for a_IA in a.getInDeAgent():
                if a_IA.getBelongTo().id != vertext.id:
                    commCost = commCost + vertext.connectedTo[a_IA.getBelongTo()]
        return commCost

    def moveGtoTarget(self, G, target):
        for a in G:
            target.addAgent(a)
            self.currentVertext.delAgent(a)