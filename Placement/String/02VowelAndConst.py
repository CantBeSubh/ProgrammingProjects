import re
def solve(A):
    vowel='[aeiou]'
    const='[^aeiou]'
    c=0
    n=len(A)
    for i in range(n):
        for j in range(i+1,n):
            if(re.search(vowel,A[i]) and re.search(vowel,A[j]) ) or (re.search(const,A[i]) and re.search(const,A[j])):
                pass
            else:
                c+=1
    
    return c%(10**9+7)

def solve2(a):
    vowel='[aeiou]'
    const='[^aeiou]'
    n=len(a)
    v=0
    c=0
    count=0
    for i in a:
        if re.search(vowel,i):
            v+=1
            if c>0:
                count+=c
        else:
            c+=1
            if v>0:
                count+=v

    return count
    
print(solve2('abcdabe'))