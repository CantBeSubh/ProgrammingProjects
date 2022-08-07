def isSubsequence(s: str, t: str) -> bool:
    i,j=0,0
    while i<len(s) and j<len(t):
        if t[j]==s[i]:
            i+=1
            j+=1
        else:
            j+=1
    return True if i==len(s) else False

print(isSubsequence('aaaaaa','bbaaaa'))