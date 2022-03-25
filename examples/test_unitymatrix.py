from src import unitymatrix as uni        #csrmatrix imported in unitymatrix

print(uni.csr.csr_matrix.toarray(uni.I(7)))        #default delta=1

print(uni.csr.csr_matrix.toarray(uni.I(7, 8)))    #delta=8
