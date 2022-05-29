graph={
    'a':['b','c','d'],
    'b':['e'],
    'c':['d','e'],
    'd':[],
    'e':[]
}
visited=set()

def dfs(visited,graph,ref):
    if ref not in visited:
        print(ref)
        visited.add(ref)
        for neighbour in graph[ref]:
            dfs(visited,graph,neighbour)
        
    

dfs(visited,graph,'a')