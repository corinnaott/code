from src import tridiagtoep as tri

toepdata = [2, 3, 1]  #= [diag val, upper val, under val]
T = tri.tridiagtoep(5, toepdata)

print("T.data=",T.data,", T.indices=", T.indices, ", T.indptr=",T.indptr, ", T.shape=",T.shape)
print(tri.csr.csr_matrix.toarray(T))