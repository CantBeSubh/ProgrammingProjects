#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        r=[]
        # code here
        zero=arr.count(0)
        one=arr.count(1)
        two=arr.count(2)
        r=[0]*zero+[1]*one+[2]*two
        return r
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        arr=ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends