def soln(n):
    res = []
    res.append([1])
    for i in range(1, n):
        temp = [1] * (i + 1)
        for j in range(1, i):
            temp[j] = res[-1][j - 1] + res[-1][j]
        res.append(temp)
    return res


def best_soln(n):
    res = []
    for i in range(n):
        temp = [1]
        ans = 1
        for j in range(1, i + 1):
            ans *= (i + 1) - j
            ans //= j
            temp.append(ans)
        res.append(temp)
    return res


print(best_soln(5))
