#https://leetcode.com/problems/find-the-duplicate-number/

# def func(arr):
#     n=len(arr)
#     M=-1
#     S=0
#     for i in arr:
#         S+=i
#         M=i if i>M else M
#     e=n-M
#     s=M*(M+1)/2

#     return (S-s)//e

def func(arr):
    n=len(arr)
    s=0
    for i in arr:
        s+=i
    return int(round(s/n))

    
print(func([1,4,4,2,4]))