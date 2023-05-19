t = int(input())
while t:
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    for i in range(n):
        if abs(a[i] - b[i]) > k:
            for j in range(i + 1, n):
                if abs(a[i] - b[j]) <= k:
                    b[i], b[j] = b[j], b[i]
                    break
    print(*b, sep=" ")
    t -= 1
