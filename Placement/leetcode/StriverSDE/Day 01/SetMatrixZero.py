def better_soln(matrix):
    n = len(matrix)
    m = len(matrix[0])
    r = [0] * n
    c = [0] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                r[i] = 1
                c[j] = 1
    for i in range(n):
        for j in range(m):
            if r[i] == 1 or c[j] == 1:
                matrix[i][j] = 0

    return matrix


def best_soln(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col0 = 1
    # r = [0] * n ->matrix[0][..]
    # c = [0] * m ->matrix[..][0]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                if j == 0:
                    col0 = 0
                else:
                    matrix[i][0] = 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(m):
            matrix[0][i] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix
