class Vertex:
    def __init__(self,data):
        self.vertex=data
        self.next=None

class Graph:
    def __init__(self,vertices):
        self.nV=vertices
        self.graph=[None]*self.nV

    def add_edge(self,src,dest):
        node=Vertex(src)
        node.next=self.graph[dest]
        self.graph[dest]=node

    def print(self):
        for i in range(self.nV):
            print('List of vertex {} '.format(i),end='')
            temp=self.graph[i]
            while temp:
                print('-> {}'.format(temp.vertex),end='')
                temp=temp.next
            print('\n')
    # def add_edge(self,src,dest):
    #     self.graph[src]=Vertex(src)
    #     d=Vertex(dest)
    #     self.graph[src].next=d


graph=Graph(5)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,0)
graph.add_edge(1,3)
graph.print()