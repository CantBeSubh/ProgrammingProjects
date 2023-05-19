def solve(str, n):
    s = set()
    for i in range(n - 1):
        s.add(str[i : i + 2])
    return len(s)


t = int(input())
while t:
    n = int(input())
    s = input()
    print(solve(s, n))
    t -= 1
