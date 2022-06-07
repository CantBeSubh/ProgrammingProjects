def factorial(N):
    def factR(N):
        if N==1: return 1
        return N*factR(N-1)
    return factR(N)

print(factorial(5))