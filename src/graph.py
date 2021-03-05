from src.vertext import *

'''
Graph包含了所有的顶点
包含了一个主表(临接列表)
'''
class Graph():  # 图 => 由顶点所构成的图

    '''
    存储图的方式是用邻接表实现的.

    数据结构: {
                key:Vertext(){
                    self.id = key
                    self.connectedTo{
                        相邻节点类实例 : 权重
                        ..
                        ..
                    }
                }
                ..
                ..
        }
    '''

    def __init__(self):
        self.vertList = {}  # 临接列表
        self.numVertices = 0  # 顶点个数初始化

    def addVertex(self, key, capablities):  # 添加顶点
        self.numVertices = self.numVertices + 1  # 顶点个数累加
        newVertex = Vertext(key, capablities)  # 创建一个顶点的临接矩阵
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):  # 通过key查找定点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):  # transition:包含 => 返回所查询顶点是否存在于图中
        # print( 6 in g)
        return n in self.vertList

    def addEdge(self, f, t, cost=0):  # 添加一条边.
        ''' 因为相比较于普通的图，此算法用到的图每个结点还要携带capabilities，所以需要在添加边之前对结点进行初始化，
            而不能在添加边的时候初始化，不然此处还要提供多个参数，不合理。
        if f not in self.vertList:  # 如果没有f结点,就创建一个f结点
            nv = self.addVertex(f)
        if t not in self.vertList:  # 如果没有t结点,就创建一个t结点
            nv = self.addVertex(t)
        '''
        flag=0   #flag=0 边两端结点都存在 | flag=1 起点不存在  |flag=2 终点不存在
        if f not in self.vertList:  # 如果没有f结点,就提示无该节点
            flag = 1
            print("pls add the first vertex node!")
        if t not in self.vertList:  # 如果没有t结点,就提示无该节点
            flag = 2
            print("pls add the second vertex node!")

        if flag==0:
            if cost == 0:  # cost == 0 代表是没有传入参数,而使用的默认参数0,即是是无向图
                self.vertList[f].addNeighbor(self.vertList[t], cost)  # cost是权重.无向图为0
                self.vertList[t].addNeighbor(self.vertList[f], cost)
            else:  # cost传入值代表是有向图，只需要为起点结点添加权重标识
                self.vertList[f].addNeighbor(self.vertList[t], cost)  # cost是权重

    def getVertices(self):  # 返回图中所有的定点
        return self.vertList.keys()

    def __iter__(self):  # return => 把顶点一个一个的迭代取出.  note:此处返回的是一个存放有顶点数值的迭代器，可以用此迭代器对其值进行遍历
        return iter(self.vertList.values())

