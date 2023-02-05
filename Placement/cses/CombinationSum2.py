res = list()


def soln(c, b, arr):
    if sum(c) == b:
        c.sort()
        res.append(c)
        return
    if sum(c) > b:
        return
    if len(arr) == 0:
        return
    c1 = c[:]
    c2 = c[:]
    c2.append(arr[0])
    soln(c1, b, arr[1:])
    soln(c2, b, arr[1:])
    return


def combinationSum2(A, B):
    A.sort()
    soln([], B, A)
    return res


if __name__ == "__main__":
    A = [10, 1, 2, 7, 6, 1, 5]
    B = 8
    print(combinationSum2(A, B))
