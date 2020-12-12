
def zero_matrix(matrix):

    rows = []
    cols = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in rows or j in cols:
                matrix[i][j] = 0
