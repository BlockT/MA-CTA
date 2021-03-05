class Subtask():

    def __init__(self,key, req_capab):
        self.id = key
        self.req_capab = req_capab
        self.belongToAgent = None
        self.interDependTask = ()


    def getId(self):
        return self.id

    def getReqCapab(self):
        return self.req_capab

    def setBelongTo(self,belong):
        self.belongToAgent = belong

    def getBelongTo(self):
        return self.belongToAgent

    def setInDeTask(self,interDenpendTask):
        self.interDependTask=interDenpendTask

    def getInDeTask(self):
        return self.interDependTask

