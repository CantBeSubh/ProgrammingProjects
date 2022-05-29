#graph using dictionary
def bfs(graph,ref):
    visited=set()
    queue=[ref]
    while queue:

        a=queue.pop(0)
        visited.add(a)
        for i in graph[a]:
            if i not in visited:
                queue.append(i)
    print(visited)
graph={
    0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}

bfs(graph,0)