from examples import test_csrmatrix
from examples import test_tridiagtoep
from examples import test_unitymatrix
from examples import test_linalg

from examples import test_relaxedrichardson_iterativesolver
    #, test_relaxedrichardson_iterativesolver, test_tridiagtoep, test_unitymatrix

#--------------------------------------

#test class csr_matrix
#print("test csr_matrix:")
#print("__init__:","data list:", A.data, ", indices list:", A.indices,", indptr list", A.indptr,", shape tuple",  A.shape)
#print("toarray():","full matrix A:", csr.csr_matrix.toarray(A), ",full matrix B:", csr.csr_matrix.toarray(B))
#print("__matmul__ / @ operator:", csr.csr_matrix.__matmul__(A,b), "equals" , A@b)
#print("__add__ / + operator:" , csr.csr_matrix.toarray(csr.csr_matrix.__add__(A, B)), "equals", csr.csr_matrix.toarray(A+B))

#test linalg
##vector
#print("vector(): v=" ,v )
#print("vecdim(): vecdim(v)=" , la.vecdim(v))
##vector dimension #alpha=2.5
#print("scal(): scal(alpha, v)=", la.scal(alpha, v))
##vector addition
#print("axpy(): only vectors: axpy(v, w [,alpha=1.0])=",la.axpy(v,w),"/ with scalar alpha: axpy(v, w, alpha)=", la.axpy(v, w, alpha))
##norm #x = la.vector(5 ,3, 2**0.5)
#print("nrm(): nrm(x)=", la.nrm(x) , "  ( = (5**2 + 3**2 + (2**0.5)**2)**0.5 = (25+9+2)**0.5 = 36**0.5  )" )
##matrix vector multiplication
#print("csrvm(): csrvm(A2, x2)=", la.csrmv(A2, x2))



