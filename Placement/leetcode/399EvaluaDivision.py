def solve(equations, values, queries):
    m = dict()
    n = len(values)
    # for i in range(n):
    #     m[(equations[i][0], equations[i][1])] = values[i]
    #     m[(equations[i][1], equations[i][0])] = 1 / values[i]

    # res = []
    # for i in queries:
    #     if i[0] == i[1]:
    #         res.append(float(1))
    #     elif (i[0], i[1]) in m:
    #         res.append(float(m[(i[0], i[1])]))
    #     else:
    #         res.append(float(-1))
    # return res
    for i in range(n):
        if equations[i][0] not in m:
            m[equations[i][0]] = values[i]
        else:
            m[equations[i][1]] = m[equations[i][0]] / values[i]
            continue

        if equations[i][1] not in m:
            m[equations[i][1]] = 1
        else:
            m[equations[i][0]] = values[i] * m[equations[i][1]]
            continue

    res = []
    for i in queries:
        if i[0] not in m or i[1] not in m:
            res.append(float(-1))
        elif i[0] == i[1]:
            res.append(float(1))
        else:
            res.append(m[i[0]] / m[i[1]])

    print(m)
    return res


print(
    solve(
        [["a", "b"], ["e", "f"], ["b", "e"]],
        [3.4, 1.4, 2.3],
        [
            ["b", "a"],
            ["a", "f"],
            ["f", "f"],
            ["e", "e"],
            ["c", "c"],
            ["a", "c"],
            ["f", "e"],
        ],
    )
)

from typing import List


class Solution:
    def dfs(
        self, node: str, dest: str, gr: dict, vis: set, ans: List[float], temp: float
    ) -> None:
        if node in vis:
            return

        vis.add(node)
        if node == dest:
            ans[0] = temp
            return

        for ne, val in gr[node].items():
            self.dfs(ne, dest, gr, vis, ans, temp * val)

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict:
        gr = {}

        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in gr:
                gr[dividend] = {}
            if divisor not in gr:
                gr[divisor] = {}

            gr[dividend][divisor] = value
            gr[divisor][dividend] = 1.0 / value

        return gr

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        gr = self.buildGraph(equations, values)
        finalAns = []

        for query in queries:
            dividend, divisor = query

            if dividend not in gr or divisor not in gr:
                finalAns.append(-1.0)
            else:
                vis = set()
                ans = [-1.0]
                temp = 1.0
                self.dfs(dividend, divisor, gr, vis, ans, temp)
                finalAns.append(ans[0])

        return finalAns
