def soln(x, n):
    if n == 0:
        return 1
    if n < 0:
        return float(1 / soln(x, abs(n)))
    return x * soln(x, n - 1)


print(soln(2, -2))
