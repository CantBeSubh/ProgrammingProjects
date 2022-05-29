def odd_or_even(arr):
    ans=[]
    for i in arr:
        ans+=i
    return "even" if abs(ans)%2==0 else "odd"