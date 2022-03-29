from src import tridiagtoep as tri
print("Tridiagonal Toeplitz Matrix:")

toepdata = [2, 3, 1]  #= [diag val, upper val, under val]
T = tri.tridiagtoep(5, toepdata)

print("for toepdata=[2, 3, 1] and n=5: ")
print("T = tri.tridiagtoep(5, toepdata) =", tri.csr.csr_matrix.toarray(T))
print("T.data=",T.data,", T.indices=", T.indices, ", T.indptr=",T.indptr, ", T.shape=",T.shape)

print("--------------------------------------------------------------------------------------------------------------------")
#help(tri.tridiagtoep)