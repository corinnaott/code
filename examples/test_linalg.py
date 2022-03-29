from src import linalg as la
print("linalg: ")

v1 = 4
v2 = 9
v3 = 88-9
v4 = 2**(1/2)
v = la.vector(v1, v2, v3, v4, 1)
print("vector(): for v1=4, v2= 9, v3=88-9, v4=2**(1/2): v = vector(v1, v2, v3, v4, 1)=" ,v )
print("vecdim(): vecdim(v)=" , la.vecdim(v))

alpha = 2.5
print("scal(): scalar multiplication: for alpha=2.5 and vector v: scal(alpha, v)= alpha*v= ", la.scal(alpha, v))

w = la.vector(1, 1, 1, 1, 1)
print("axpy(): addition of vectors vectors v and w=[1, 1, 1, 1, 1]: axpy(v, w [,alpha=1.0])= v+w = ",la.axpy(v,w)
      ,"/optional: with scalar alpha=2.5: axpy(v, w, alpha)= alpha*v +w =", la.axpy(v, w, alpha))

x = la.vector(5 ,3, 2**0.5)
print("nrm(): Euclid norm of vector x=[5, 3, 2**0.5]: nrm(x)=", la.nrm(x) , "  ( = (5**2 + 3**2 + (2**0.5)**2)**0.5 = (25+9+2)**0.5 = 36**0.5  )" )



from src import csrmatrix as csr
A2_data = [10, -2, 3, 9, 7, 8, 7, 3, 8, 7, 5, 8, 9, 13]
A2_indices = [0, 4, 0, 1, 1, 2, 3, 0, 2, 3, 4, 1, 3, 4]
A2_indptr = [0, 2, 4, 7, 11, 14]
A2_shape = (5,5)
A2 = csr.csr_matrix((A2_data, A2_indices, A2_indptr), A2_shape)

#Matrix A2 and vector w
print("csrvm(): matrix vector product of matrix A2=", csr.csr_matrix.toarray(A2) ," and vector w: csrvm(A2, w)= A2*w =", la.csrmv(A2, w))


print("----------------------------------------------------------------------------------------------------------------")