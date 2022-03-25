def vector(scalar1, scalar2, *scalars):
    """Vector instantiation.

    Builds vector v=(v1, v2, ...)T based on given scalars.

    Parameters
    ----------
    scalar1 : float/ int
        Scalar v1.
    scalar2 : float/ int
        Scalar v2.
    *scalars : float/ int
        Any other scalars v3, v4,...

    Returns
    -------
    vector : list
        Scalars are elements of this list.

    """
    vector = [scalar1, scalar2, *scalars]
    return vector

def vecdim(vector):
    """Dimension of given vector.

    Parameters
    ----------
    vector : list
        Given vector.

    Returns
    -------
    len(vector): int
        Number of elements/scalars of vector.

    """
    return len(vector)

def scal(alpha, x):
    """Scalar multiplication.

    Vector x multiplied by alpha.

    Parameters
    ----------
    alpha : float
        Scalar.
    x : list
        vector.

    Returns
    -------
    scalvec : list
        Vector.

    """
    scalvec = []
    for i in x:
        productia = i * alpha
        scalvec.append(productia)
    return scalvec


def axpy(x, y, alpha=1.):
    """Addition of vectors.

    Parameters
    ----------
    x : list
        Vector.
    y : list
        Vector.
    alpha : float/ int, optional
        For scalar multiplicaton: vector x multplied by alpha. The default is 1..

    Returns
    -------
    addvec : list
        Vector.

    """
    alphax = []
    for i in x:  # scalar multiplication of x by alpha
        productia = i * alpha
        alphax.append(productia)

    addvec = []
    for i in range(len(y)):
        sumi = alphax[i] + y[i]  # adds scalars of alpha x and y from same position/ index
        addvec.append(sumi)
    return addvec


def nrm(x):
    """Euclid norm of a vector.

    Parameters
    ----------
    x : list
        Vector.

    Returns
    -------
    normx : float
        Euclid norm.

    """
    quad = []
    for i in x:
        quad = quad + [i**2]       #in square root
    norm = sum(quad) ** 0.5
    return norm



def csrmv(A, x):            #similar to __matmul__ in class csr_matrix
    """
    Matrix-vector product.

    Parameters
    ----------
    A : csr_matrix
        Matrix in CSR format.
    x : list
        Vector.

    Returns
    -------
    mvp : list
        Vector Ax.
    """
    m = A.shape[0]    #like toarray in class csr-matrix
    n = A.shape[1]
    rows = []
    for i in range(m):
        row_helper = [0]*n
        for l in range(A.indptr[i], A.indptr[i+1]):
            row_helper[A.indices[l]] = A.data[l]
        rows = rows + [row_helper]

    mvp = []        #matrix vector product
    y = 0
    for i in rows:
        j = 0
        for l in i:
            y = y + l* x[j]
            j = j + 1
        mvp = mvp + [y]
        y = 0
    return mvp
