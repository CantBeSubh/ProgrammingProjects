# def dp(arr, out, n):
#     if not arr:
#         if sum(out) <= n:
#             return 1
#         return 0
#     # temp1 = out
#     temp2 = out.copy()
#     temp2.append(arr[0])
#     arr = arr[1:]
#     return dp(arr, out, n) + dp(arr, temp2, n)


# def solve(n, k):
#     arr = [2**x for x in range(k)]
#     return dp(arr, [], n)


def solve(n, k):
    for i in range(k):
        s = 2 ** (i + 1) - 1
        if s > n:
            return 2 ** (i)
    return 2**k


t = int(input())

while t:
    n, k = map(int, input().split())
    print(solve(n, k))
    t -= 1
