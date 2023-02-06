def isPalindrome(s):
    return s == s[::-1]


def soln(ip):
    c = 0
    for i in ip:
        if isPalindrome(i):
            c += 1
    if c == 0:
        return 1000
    if c == len(ip):
        return c
    for i in ip:
        if not isPalindrome(i):
            x=999
            for j in range(1,len(i)):
                


def palindromicPartition(s):
    pass


if __name__ == "__main__":
    s = input()
    print(palindromicPartition(s))
