from src import linalg as la

v1 = 4
v2 = 9
v3 = 88-9
v4 = 2**(1/2)
v = la.vector(v1, v2, v3, v4, 1)
print("vector(): v=" ,v )
print("vecdim(): vecdim(v)=" , la.vecdim(v))

alpha = 2.5
print("scal(): scal(alpha, v)=", la.scal(alpha, v))

w = la.vector(1, 1, 1, 1, 1)
print("axpy(): only vectors: axpy(v, w [,alpha=1.0])=",la.axpy(v,w),"/ with scalar alpha: axpy(v, w, alpha)=", la.axpy(v, w, alpha))

x = la.vector(5 ,3, 2**0.5)
print("nrm(): nrm(x)=", la.nrm(x) , "  ( = (5**2 + 3**2 + (2**0.5)**2)**0.5 = (25+9+2)**0.5 = 36**0.5  )" )



from src import csrmatrix as csr
A2_data = [10, -2, 3, 9, 7, 8, 7, 3, 8, 7, 5, 8, 9, 13]
A2_indices = [0, 4, 0, 1, 1, 2, 3, 0, 2, 3, 4, 1, 3, 4]
A2_indptr = [0, 2, 4, 7, 11, 14]
A2_shape = (5,5)
A2 = csr.csr_matrix((A2_data, A2_indices, A2_indptr), A2_shape)
x2 = la.vector(1, 1, 1, 1, 1)
#Matrix A2 and vector x2
print("csrvm(): csrvm(A2, x2)=", la.csrmv(A2, x2))

