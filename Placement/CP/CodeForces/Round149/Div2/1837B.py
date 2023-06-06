t = int(input())

while t:
    n = int(input())
    s = input()

    ans = 0
    stack = []
    for i in range(n):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.append(s[i])
            else:
                stack.pop()
                if not stack and ans == 0:
                    ans += 2
                elif stack and ans == 0:
                    ans += 3
    if ans == 0:
        ans = len(stack) + 1
    print(ans)

    t -= 1
