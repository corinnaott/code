from src import csrmatrix as csr
print("csr_matrix class:")

A_data = [10, -2, 3, 9, 7, 8, 7, 3, 8, 7, 5, 8, 9, 13]
A_indices = [0, 4, 0, 1, 1, 2, 3, 0, 2, 3, 4, 1, 3, 4]
A_indptr = [0, 2, 4, 7, 11, 14]
A_shape = (5,5)
A = csr.csr_matrix((A_data, A_indices, A_indptr), A_shape)

B_data = [1, 2, 1, 3, 4, 5, 1, 2, 4, 3]
B_indices = [1, 2, 0, 1, 2, 3, 1, 4, 2, 3]
B_indptr = [0, 2, 5, 6, 8, 10]
B_shape = (5,5)
B = csr.csr_matrix((B_data, B_indices, B_indptr), B_shape)

b = [1, 1, 1, 1, 1]   #vector

print("__init__: data list: A.data =", A.data, ", indices list: A.indices =", A.indices,", indptr list: A.indptr =", A.indptr,", shape tuple (m, n)=",  A.shape)

print("toarray(): matrix A: csr_matrix.toarray(A):", csr.csr_matrix.toarray(A), ",matrix B: csr_matrix.toarray(B):", csr.csr_matrix.toarray(B))

print("__matmul__ / @ operator: matrices A and vector b=[1, 1, 1, 1, 1]: csr.csr_matrix.__matmul__(A,b) = A*b =", csr.csr_matrix.__matmul__(A,b), "and A@b =" , A@b)

print("__add__ / + operator: matrix A and B: csr.csr_matrix.toarray(csr.csr_matrix.__add__(A, B)) = A+B =" , csr.csr_matrix.toarray(csr.csr_matrix.__add__(A, B)), "and csr.csr_matrix.toarray(A+B) =", csr.csr_matrix.toarray(A+B))

print("----------------------------------------------------------------------------------------------------------------------")
