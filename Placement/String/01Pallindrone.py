import re
def isPalindrome(A):
    i=0
    j=len(A)-1
    ignoreMe='[a-zA-Z0-9]'
    while(i<=j):
        if not(re.search(ignoreMe,A[i])):
            i+=1
        elif not(re.search(ignoreMe,A[j])):
            j-=1
        else:
            if A[i].lower()!=A[j].lower():
                return 0
            i+=1
            j-=1
    return 1

print(isPalindrome('A man, a plan, a canal: Panama'))