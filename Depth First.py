from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited[v]=True
        print(v,end=' ')
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    def DFS(self):
        v=len(self.graph)
        visited=[False]*(v)
        for i in range (v):
            if visited[i]==False:
                self.DFSUtil(i,visited)

g=graph()
g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(2,0)
g.add(2,3)
g.add(3,3)
print("following is depth first traversal")
g.DFS()
            
