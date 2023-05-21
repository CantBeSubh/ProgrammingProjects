def minLength(s: str) -> int:
    s = s.lower()
    for _ in range(len(s)):
        s = s.replace("ab", "")
        s = s.replace("cd", "")
    return len(s)


print(minLength("ABFCACDB"))
