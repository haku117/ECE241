import sys

INFINITY = sys.maxsize

class HeapPriorityQueue:

    def __init__(self,):
        self.heapArray = []
        self.currentSize = len(self.heapArray)


    def heapInsert(self,arr):

        for i in arr:
            self.heapArray.append(i)
            self.currentSize = self.currentSize + 1
            self.count = 0
            self.constructHeap()


    def heapify(self,n, i):

        smallest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and self.heapArray[i][0] > self.heapArray[l][0]:
            smallest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and self.heapArray[smallest][0] > self.heapArray[r][0]:
            smallest = r

        # Change root, if needed
        if smallest != i:
            self.heapArray[i], self.heapArray[smallest] = self.heapArray[smallest], self.heapArray[i]  # swap
            # Heapify the root.
            self.heapify(n, smallest)  # heap for one entry


    def constructHeap(self):
        # Build a min heap.
        for i in range(int(self.currentSize/2), -1, -1):
            self.heapify(self.currentSize, i)


    def decreaseKey(self,val,amt):
        # this is a little wierd, but we need to find the heap thing to decrease by
        # looking at its value
        done = False
        i = 0
        myKey = 0
        while not done and i < self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1])

        self.constructHeap()
        # print("After decreaseKey:{}".format(self.heapArray))


    def popMin(self):

        if self.heapArray:
            self.constructHeap()
            last = self.heapArray.pop()
            self.currentSize -= 1
            if self.currentSize > 0:
                current= self.heapArray[0]
                self.heapArray[0] = last
            else:
                current=last

        return current


    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False



class Vertex:


    def __init__(self,key):
        """
        self.id stores the id of the node from where we start Dijkstras
        self.connectedTo stores key='destination node_id'  and value=['distance form start',['nodes in the path']]
        
        e.g. print(g.getVertex('V0').connectedTo) 
        self.id='V0'
        self.connectedTo={'V1':[1],'V2':[2],'V3':[2,[V1]],'V4':[2,[V3,V1]],'V5':[3,['V2']]}
        """
        self.id = key
        self.connectedTo = dict()
        # self.prev=[]


    def addPath(self, nbr, weight=INFINITY):
        try:
            if self.connectedTo[nbr] > weight:
                self.connectedTo[nbr] = [weight]
        except KeyError:
            self.connectedTo[nbr] = [weight]


    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str(["node:{},distance:{}".format(x,self.connectedTo[x]) for x in self.connectedTo])


    def getConnections(self):
        return [conn for conn in self.connectedTo.keys() if self.connectedTo[conn][0] < INFINITY]


    def getId(self):
        return self.id


    def getWeight(self,nbr):
        return self.connectedTo[nbr][0]


    def getPreds(self):
        """
    E.g.:
        for the case of
        g.addEdge(V0, V1,1)
        g.addEdge(V0, V2,2)
        g.addEdge(V1, V3,1)
        g.addEdge(V3, V4,1)
        g.addEdge(V2, V5,1)
        
        g.dijkstra(g.getVertex('V0'))
        
        print(g.getVertex('V0').connectedTo) gives {'V1':[1],'V2':[2],'V3':[2,['V1']],'V4':[2,['V3','V1']],'V5':[3,['V2']]}
        print(g.getVertex('V0').getPreds() gives ['V1','V3,'V1',V2']
        """
        pred_list=[]

        for nbr in self.connectedTo:
            if len(self.connectedTo[nbr])>1:
                pred_list.extend(self.connectedTo[nbr][1])

        return pred_list



class DijkstraGraph:
    """
E.g.:
        for the case of
        g.addEdge(V0, V1,1)
        g.addEdge(V0, V2,2)
        g.addEdge(V1, V3,1)
        g.addEdge(V3, V4,1)
        g.addEdge(V2, V5,1)
        
        g.dijkstra(g.getVertex('V0'))
        
        print(g.getVertex('V0').connectedTo) gives {'V1':[1],'V2':[2],'V3':[2,['V1']],'V4':[2,['V3','V1']],'V5':[3,['V2']]}
    """

    def __init__(self):
        """
        self.vertList stores node_id as key and node as value
        e.g.
        {'V0':<__main__.Vertex instance at 0x7fda44505c68>,'V1':<__main__.Vertex instance at 0x7fda44505cb0>}
        """
        self.vertList = dict()
        self.numVertices = 0


    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex


    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None


    def __contains__(self,n):
        return n in self.vertList.keys()


    def addEdge(self,f,t,cost=INFINITY):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addPath(self.vertList[t].id, cost)


    def populatePaths(self):
        """
        creates a mesh (distance from every node to every node)
        sets cost to infinity for disconnected nodes
        """
        cost = INFINITY
        for f in self.vertList:
            for e in self.vertList:
                try:
                    self.vertList[f].connectedTo[e]
                except KeyError:
                    if f == e:
                        self.vertList[f].addPath(self.vertList[e].id, 0)
                    else:
                        self.vertList[f].addPath(self.vertList[e].id, cost)


    def getVertices(self):
        return self.vertList.keys()


    def getDistance(self,start=None,to=None):
        # if (start in self.vertList) and (to in self.vertList):
        return self.vertList[start].getWeight(to)
        # else:
        #     return None


    def setDistance(self,start=None,to=None,dist=INFINITY):
        # TODO: fill this function
        """
        Don't return anything
        Vertex object has self.connectedTo member variable which consists of
        ['distance form start',['nodes in the path']]
        
        This function assigns the 'distance form start'  
        """
        pass # TODO remove this after filling the function


    def setPred(self,start=None,to=None,pred=None):
        # TODO: fill this function
        """
        Don't return anything
        Vertex object has self.connectedTo member variable which consists of
        ['distance form start',['nodes in the path']]
        
        This function creates/populates the ['nodes in the path'] 
        """
        pass # TODO remove this after filling the function


    def __iter__(self):
        return iter(self.vertList.values())


    def dijkstra(self,start):
        # TODO: fill this function
        """
        Don't return anything
        
        Implement Dijktras:
        0. Call self.populatePaths()
        1. Use the HeapPriorityQueue and it functions:(heapInsert,popMin,decreaseKey)
        2. Use the DijkstraGraph functions:(getDistance, getWeight, setDistance, setPred)
        """
        pass # TODO remove this after filling the function

                        
                        
    def betweenness_func(self):
        # TODO: fill this function
        """ 
        return max_bc_node_id, dictionary_of_betweenness 
        
        Nomenclature:
        
        E.g.:
        for the case of
        g.addEdge('V0', 'V1',1)
        g.addEdge('V0', 'V2',2)
        g.addEdge('V1', 'V3',1)
        g.addEdge('V3', 'V4',1)
        g.addEdge('V2', 'V5',1)
        
        g.dijkstra(g.getVertex('V0'))
        
        print(g.getVertex('V0').connectedTo) gives {'V1':[1],'V2':[2],'V3':[2,['V1']],'V4':[2,['V3','V1']],'V5':[3,['V2']]}
        
        node_id: name of the node with maximum betweenness. e.g node_id = 'V1'
        
        dictionary_of_betweenness: dictionary with key as node_id and value 
        as number of times node_id is a predecessor in all shortest paths.
        e.g dictionary_of_betweenness={'V1':2,'V2':1,'V3':1} 
        """
                
        return max_bc_node_id,dictionary_of_betweenness



######################### Test your code below #########################


def check_dijkstra():
    g = DijkstraGraph()
    g.addEdge('V0','V1',5)
    g.addEdge('V0','V5',1)
    # g.addEdge('V1','V2',4)
    # g.addEdge('V2','V3',9)
    # g.addEdge('V3','V4',7)
    # g.addEdge('V3','V5',3)
    # g.addEdge('V4','V0',1)
    # g.addEdge('V1','V2',1)
    g.addEdge('V5','V2',3)
    # g.addEdge('V2', 'V6', 1)
    # g.addEdge('V1','V4',8)
    # g.addEdge('V4', 'V7', 1)

    g.dijkstra(g.getVertex('V0'))
    ##############
   
    print(g.getVertex('V0').connectedTo)


def check_betweenness():
    g = DijkstraGraph()
    g.addEdge('V0','V1',5)
    g.addEdge('V0','V5',1)
    # g.addEdge('V1','V2',4)
    # g.addEdge('V2','V3',9)
    # g.addEdge('V3','V4',7)
    # g.addEdge('V3','V5',3)
    # g.addEdge('V4','V0',1)
    # g.addEdge('V1','V2',1)
    g.addEdge('V5','V2',3)
    # g.addEdge('V2', 'V6', 1)
    # g.addEdge('V1','V4',8)
    # g.addEdge('V4', 'V7', 1)

    # print(g.getVertex('V0').connectedTo, g.vertList)
    bc_node,bc_count_dict= g.betweenness_func()
    
    print(bc_node,bc_count_dict)
    #print(g.vertList)
    # print(g.getVertex('V0'))


if __name__ == '__main__':
    #check_dijkstra()
    #check_betweenness()
    print("Testing")
