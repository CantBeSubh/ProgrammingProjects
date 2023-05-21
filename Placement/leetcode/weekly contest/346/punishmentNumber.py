def chk(n: int) -> bool:
    p = n * n
    if n == p:
        return True

    p = str(p)
    res = 0
    for j in p:
        res += int(j)
    if res == n:
        return True

    for i in range(1, len(p)):
        for j in range(len(p) - i):
            res -= int(p[j])
            res -= int(p[j + i])
            temp = int(p[j : j + i + 1])
            if res + temp == n:
                return True
            else:
                res += int(p[j])
                res += int(p[j + 1])

    return False


def solve(n: int) -> int:
    res = 0
    for i in range(1, n + 1):
        if chk(i):
            res += i

    return res


print(solve(10))
