def solve(x, k):
    if x == 0:
        return 0, []
    if x < k:
        return 1, [x]
    res = []
    i = x
    while x > 0:
        if i % k != 0:
            res.append(i)
            x -= i
            i = x
        else:
            i -= 1

    return len(res), res


t = int(input())
while t:
    x, k = map(int, input().split())
    cnt = 0
    res = []
    cnt, res = solve(x, k)
    print(cnt)
    print(*res, sep=" ")
    t -= 1
