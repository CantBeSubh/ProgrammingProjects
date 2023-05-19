def dfs(graph, groups, i):
    for j in graph[i]:
        if groups[j] == groups[i]:
            return False
        if groups[j] == 0:
            groups[j] = 3 - groups[i]
            if not dfs(graph, groups, j):
                return False
    return True


def isBipartite(graph) -> bool:
    # 0: unvisited, 1: group 1, 2: group 2
    groups = [0] * len(graph)
    for i in range(len(graph)):
        if groups[i] == 0:
            groups[i] = 1
            if not dfs(graph, groups, i):
                return False
    return True
