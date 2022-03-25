from src import csrmatrix as csr

def tridiagtoep(n, toepdata):
    """Tridiagonal Toeplitz matrix.

    Parameters
    ----------
    n : int
        Shape of matrix will be (n,n).
    toepdata : list
        Supposed to contain 3 elements; data = [value on diagonal, upper value, under value].

    Returns
    -------
    toeplitz : csr_matrix
        Instantiated CSR matrix.

    """
    data = toepdata * (n - 1) + [toepdata[0]]

    indptr = [0, 2]  # 2 elements in first row
    x = 2
    for i in range(n - 2):
        x = x + 3  # 3 elements in middle rows
        indptr = indptr + [x]
    indptr = indptr + [x + 2]  # 2 elements in last row

    indices = [0, 1]  # first row indices
    for i in range(n - 2):  # middle row indices
        indices = indices + [i, i + 1, i + 2]
    indices = indices + [n - 2, n-1]  # last row indices

    toeplitz = csr.csr_matrix((data, indices, indptr), (n, n))
    return toeplitz
