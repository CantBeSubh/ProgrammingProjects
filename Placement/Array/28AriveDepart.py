def func(arr,dep):
    n=len(arr)
    p=1
    for i in range(1,n):
        j=0
        while(j<n-1):
            j+=1
            if(dep[j]>arr[i]):
                if arr[i]>arr[j]:
                    p+=1
    
    return p

print(func([900,1100,1235],[1000,1200,1240]))

#discussion solution
def func2(arr,dep):
    n=len(arr)
    platform = 1
    max_platform = 1
    arr.sort()
    dep.sort()
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            platform+=1
            i+=1
        else:
            platform-=1
            j+=1
        max_platform = max(max_platform,platform)
        
    return max_platform

#editor solutions
# Python3 program to find minimum number of platforms required on a railway station
#O(N*Log(N))
def findPlatform(arr, dep, n):
    
    # Inserting all the arr. and dep. times
    # in the array times
    times = []
    for i in range(n):
        times.append([dep[i], 'd'])
        times.append([arr[i], 'a'])
        
    # Sort the array
    times = sorted(times, key = lambda x: x[1])
    times = sorted(times, key = lambda x: x[0])
    
    result, plat_needed = 0, 0

    for i in range(2 * n):
        
        # If its 'a' then add 1 to plat_needed
        # else minus 1 from plat_needed.
        if times[i][1] == 'a':
            plat_needed += 1
            result = max(plat_needed, result)
        else:
            plat_needed -= 1
    
    return result


arr = [ 900, 940, 950, 1100, 1500, 1800 ]
dep = [ 910, 1200, 1120, 1130, 1900, 2000 ]
n = len(arr)

print("Minimum Number of Platforms Required =", 
      findPlatform(arr, dep, n))

# This code is contributed by Tharun Reddy 


# Python3 program to find minimum number of platforms required on a railway station 
#O(N)
def minPlatform(arrival, departure, n):

    # As time range from 0 to 2359 in
    # 24 hour clock, we declare an array
    # for values from 0 to 2360 
    platform = [0] * 2361
    requiredPlatform = 1
    
    for i in range(n):

        # Increment the platforms for arrival 
        platform[arrival[i]] += 1

        # Once train departs we decrease the
        # platform count 
        platform[departure[i] + 1] -= 1

    # We are running loop till 2361 because
    # maximum time value in a day can be 23:60 
    for i in range(1, 2361):

        # Taking cumulative sum of 
        # platform give us required 
        # number of platform for every minute 
        platform[i] = platform[i] + platform[i - 1]
        requiredPlatform = max(requiredPlatform, 
                               platform[i])
        
    return requiredPlatform

# Driver code 
arr = [ 900, 940, 950, 1100, 1500, 1800 ] 
dep = [ 910, 1200, 1120, 1130, 1900, 2000 ]
n = len(arr) 

print("Minimum Number of Platforms Required = ", 
       minPlatform(arr, dep, n))

# This code is contributed by PawanJain1