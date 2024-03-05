def strassen_matrix_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    result = [[0 for _ in range(n)] for _ in range(n)]
    a11 = [row[:n//2] for row in A[:n//2]]
    a12 = [row[n//2:] for row in A[:n//2]]
    a21 = [row[:n//2] for row in A[n//2:]]
    a22 = [row[n//2:] for row in A[n//2:]]
    b11 = [row[:n//2] for row in B[:n//2]]
    b12 = [row[n//2:] for row in B[:n//2]]
    b21 = [row[:n//2] for row in B[n//2:]]
    b22 = [row[n//2:] for row in B[n//2:]]
    p1 = strassen_matrix_multiply(add_matrix(a11, a22), add_matrix(b11, b22))
    p2 = strassen_matrix_multiply(add_matrix(a21, a22), b11)
    p3 = strassen_matrix_multiply(a11, sub_matrix(b12, b22))
    p4 = strassen_matrix_multiply(a22, sub_matrix(b21, b11))
    p5 = strassen_matrix_multiply(add_matrix(a11, a12), b22)
    p6 = strassen_matrix_multiply(sub_matrix(a21, a11), add_matrix(b11, b12))
    p7 = strassen_matrix_multiply(sub_matrix(a12, a22), add_matrix(b21, b22))
    c11 = add_matrix(sub_matrix(add_matrix(p1, p4), p5), p7)
    c12 = add_matrix(p3, p5)
    c21 = add_matrix(p2, p4)
    c22 = add_matrix(sub_matrix(add_matrix(p1, p3), p2), p6)
    for i in range(n//2):
        for j in range(n//2):
            result[i][j] = c11[i][j]
            result[i][j + n//2] = c12[i][j]
            result[i + n//2][j] = c21[i][j]
            result[i + n//2][j + n//2] = c22[i][j]
    return result
def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]
def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = strassen_matrix_multiply(A, B)
for row in result:
    print(row)
