def maxProduct(arr, n):
    min_var = max_var = max_prod = arr[0]

    for i in range(1, n):
        
        if arr[i] < 0:
            
            min_var, max_var = max_var, min_var
            
        min_var = min(arr[i] * min_var, arr[i])
        max_var = max(arr[i] * max_var, arr[i])
        
        max_prod = max(max_prod, max_var)
    return max_prod

print(maxProduct([6, -3, -10, 0, 2],5))