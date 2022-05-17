def rotate( arr):
    
    a=arr.pop()
    arr.insert(0,a)
    return arr

print(rotate([1,2,3,4,5]))

