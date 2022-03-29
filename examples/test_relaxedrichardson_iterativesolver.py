from src import relaxedrichardson_iterativesolver as rr
print("relaxedrichardson_iterativesolver:")

n = 5


A1 = rr.tri.tridiagtoep(n,[2* n**2, -1* n**2, -1* n**2] )
b = [1]*n
x0 = [0]*n
print("matrix A1 =",rr.csr.csr_matrix.toarray(A1))
#print(A1.data, A1.indices, A1.indptr)

#print(rr.richardson(A1, b, x0, theta=.1, maxiter=500, tol=1e-08))  #overflow error: result too large => too many loops?
print("for matrix A1, dimension n=5, vector b=[1]*n, start vector x0=[0]*n, relaxation theta=0.001, error tolerance tol=tol=1e-08 (default): ")
print(rr.richardson(A1, b, x0, theta=.001, maxiter=500, tol=1e-08))    #changed relaxation #converges for n<28

print("-----")
help(rr.richardson)
#unmatching dimensions
c= [1]*(n-1)
#print(rr.richardson(A1, c, x0, theta=.001, maxiter=500, tol=1e-08))

#A2
n = 5
delta = 1
A2 = A1 + rr.uni.I(n, delta)
#print(rr.richardson(A2, b, x0, theta=.001, maxiter=500, tol=1e-08))

#help(rr.richardson)
