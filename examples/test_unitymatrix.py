from src import unitymatrix as uni        #csrmatrix imported in unitymatrix

print("unit matrix:")
print("for n=7 uni.csr.csr_matrix.toarray(uni.I(7)) =", uni.csr.csr_matrix.toarray(uni.I(7)))        #default delta=1

print("now for n=7 and optional parameter delta=8: uni.csr.csr_matrix.toarray(uni.I(7, 8)) =", uni.csr.csr_matrix.toarray(uni.I(7, 8)))    #delta=8

print("---------------------------------------------------------------------------------------------------------------------")
#help(uni.I)