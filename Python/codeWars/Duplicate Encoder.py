def duplicate_encode(w):
    w=w.lower()
    w=[x for x in w]
    a=[]
    for i in range(0,len(w)):
        if w.count(w[i])>1:
            a.append(')')
        else:
            a.append('(')
    return "".join(a)




def duplicate_encode(w):
    w=[x for x in w.lower()]
    a=[]
    for i in range(0,len(w)):
        a.append(')') if w.count(w[i])>1 else a.append('(')
    return "".join(a)