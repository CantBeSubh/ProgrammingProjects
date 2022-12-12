def sol(arr):
    if not (arr):
        return ""
    if len(arr) == 1:
        return str(arr[0])
    return str(arr[-1]) + " " + str(sol(arr[1:-1]) + " " + str(arr[0]))


a = [1, 2, 3, 4, 5]
print(a)
print(sol(a))
