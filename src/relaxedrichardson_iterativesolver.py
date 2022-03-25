from src import csrmatrix as csr, linalg as la, unitymatrix as uni, tridiagtoep as tri

def richardson(A, b, x0, theta=.1, maxiter=500, tol=1e-08):
    """Relaxed Richardson iterative solver.

    Parameters
    ----------
    A : csr_matrix
        Invertible matrix.
    b : list
        Vector.
    x0 : list
        Start vector.
    theta : float, optional
        Relaxation. The default is .1.
    maxiter : int, optional
        Max. number of iteration. The default is 500.
    tol : float, optional
        Error tolerance. The default is 1e-08.

    Returns
    -------
    x : list
        Vector; current iteration/ approximated solution.
    error : list
        Contains all residues.
    numiter : int
        Number of iterations.

    """
    error = []        #for residues
    numiter = -1
    x = x0

    if A.shape[1] == la.vecdim(b):               #if condition: only Matrix mxn and vector nx1 can be multiplied
        while numiter <= maxiter:
            x = la.axpy(la.axpy(b, A@x , -1), x, - theta)     #x-theta(Ax-b) <=> -theta(-b+Ax)+x
            residuum = la.nrm(la.axpy(b, A@x , -1))
            error = error + [residuum]
            if residuum < tol:
                break
            numiter = numiter+1   #while loop until numiter=maxiter (or residuum < 0)
    else:
        print("No solution. Shape of matrix (n) must confirm with dimension of vector.")

    return "x=", x, "error=", error, "numiter=", numiter



