def isIsomorphic(s,t):
    if len(s)==1:
        return True
    m=dict()
    S,T=0,0
    c=0
    for i in s:
        if i in m.keys():
            S*=10
            S+=m[i]
        else:
            c+=1
            m[i]=c
            S*=10
            S+=c
    c=0
    m.clear()
    for i in t:
        if i in m.keys():
            T*=10
            T+=m[i]
        else:
            c+=1
            m[i]=c
            T*=10
            T+=c
    
    return True if S==T else False

def isIsomorphic2(s,t):
    if len(s)==1:
        return True
    m=dict()
    S,T='',''
    for i,c in enumerate(s):
        if c in m.keys():
            S+=' '+str(m[c])
        else:
            m[c]=i
            S+=' '+str(i)
    m.clear()
    for i,c in enumerate(t):
        if c in m.keys():
            T+=' '+str(m[c])
        else:
            m[c]=i
            T+=' '+str(i)
    return True if S==T else False


print(isIsomorphic('paper','title'))
print(isIsomorphic2('paper','title'))