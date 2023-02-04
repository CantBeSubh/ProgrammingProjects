res = list()


def soln(o, c, op):
    if o == 0 and c == 0:
        res.append(op)
        return
    if o == 0:
        res.append(op + ")" * c)
        return
    if o == c:
        op += "("
        soln(o - 1, c, op) 
        return
    soln(o - 1, c, op + "(")
    soln(o, c - 1, op + ")")
    return


def GenrateAll(n):
    soln(n, n, "")


if __name__ == "__main__":
    GenrateAll(3)
    print(res)
