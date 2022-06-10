# //TC: O(n) , SC: O(1)

# int max_sum(int A[],int N)
# {
# int rot=0,sum=0,w=0;
# for(int i=0;i<N;i++){
#    sum+=A[i];//sum -> natural sum
#    w+=i*A[i];//w -> weighted sum
# }
# int maxSum = w;
# for(int rot=0;rot<N-1;rot++){//N-1 possible rotations considered anti clockwise
#    w += A[rot]*(N-1) - (sum-A[rot]);
#    if(w>maxSum){
#        maxSum = w;
#    }
# }
# return maxSum;
# }
def func(arr,n):
    s,w=0,0
    for i in range(n):
        s+=arr[i]
        w+=i*arr[i]

    ma=w
    for r in range(n-1):
        w += arr[r]*(n-1)-(s-arr[r])
        ma=max(ma,w)
    
    return ma

print(func([8,3,1,2],4))
