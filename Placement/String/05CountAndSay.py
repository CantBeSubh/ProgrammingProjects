def countAndSay(A):
    def counter(x):
        ans=[]
        i,k,c=0,x[0],0
        while(i<len(x)):
            if(x[i]==k):
                c+=1
                i+=1
            else:
                res=str(c)+k
                ans.append(res)
                k=x[i]
                c=0
        res=str(c)+k
        ans.append(res)
        return ''.join(ans)

    ans=['1','11','21','1211']
    z=3
    while(z<A-1):
        temp=ans[-1]
        x=counter(temp)
        ans.append(x)
        z+=1

    return ans[A-1]


def countAndSay2( A):
    if A==1:
        return '1'
    st='1'
    for i in range(A-1):
        j=0
        check=st[0]
        sst=''
        count=0
        while j<len(st):
            if st[j]==check:
                count+=1
            else:
                sst=sst+str(count)+check
                check=st[j]
                j=j-1
                count=0
            j=j+1
        sst=sst+str(count)+check
        st=sst
    return st
    
print(countAndSay(7))
print(countAndSay2(7))