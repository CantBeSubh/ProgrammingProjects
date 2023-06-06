def solve(s, n) -> str:
    if n == 2:
        return s[0]
    res = ""
    curr = 0
    i = 1
    while i < n and curr < n:
        if s[curr] == s[i]:
            res += s[curr]
            curr = i + 1
            i += 1
        i += 1
    return res


t = int(input())
while t:
    n = int(input())
    s = input()
    print(solve(s, n))
    t -= 1
