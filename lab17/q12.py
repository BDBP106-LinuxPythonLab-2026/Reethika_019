# (12) Subtract two matrices (list of lists)
def subtract_matrices(m1, m2):
    return [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]