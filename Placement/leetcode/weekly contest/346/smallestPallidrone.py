def solve(s: str) -> str:
    n = len(s)
    mid = (n - 1) // 2

    if n % 2 != 0:
        left = mid - 1
        right = mid + 1
    else:
        left = mid
        right = mid + 1

    s = list(s)

    while left >= 0 and right < n:
        if s[left] != s[right]:
            if s[left] > s[right]:
                s[left] = s[right]
            else:
                s[right] = s[left]
        left -= 1
        right += 1

    return "".join(s)


print(solve("egcfe"))
print(solve("abcd"))
print(solve("seven"))
