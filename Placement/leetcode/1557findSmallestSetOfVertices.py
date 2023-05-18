def soln(n, edges):
    ans = [x for x in range(n)]
    reachable = [0] * n
    for edge in edges:
        try:
            ans.remove(edge[1])
        except:
            pass
        reachable[edge[1]] = 1

    for i in ans:
        reachable[i] = 1

    for i in range(n):
        if reachable[i] == 0:
            ans.append(i)
    return ans
    # indegree = [0] * n
    # for edge in edges:
    #     indegree[edge[1]] += 1

    # ans = []
    # for i in range(n):
    #     if indegree[i] == 0:
    #         ans.append(i)

    # return ans


print(soln(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
print(soln(3, [[1, 2], [1, 0], [0, 2]]))
