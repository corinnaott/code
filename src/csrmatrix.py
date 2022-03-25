class csr_matrix:
    """Compressed Sparse Row matrix.

    This can  be instantiated via:
        csr_matrix((data, indices, indptr), [shape = (m,n)])

    Attributes
    ----------

    data : list
        CSR format data array of the matrix.
    indices : list
        CSR formmat indices array of the matrix.
    indptr : list
        CSR format index pointer array of the matrix.
    shape : 2-tuple
        Shape (/dimension) of the matrix, optional.


    Functions

    """

    def __init__(self, csrTuple, shape=None):
        _data, _indices, _indptr = csrTuple
        if shape:
            self.shape = shape
        self.data = _data
        self.indices = _indices
        self.indptr = _indptr

    def toarray(self):
        """CSR matrix array.

        Function arrays full matrix based on csr_matrix.

        Parameters
        ----------
        A : csr_matrix
            Contains lists of data, indices, indptr as well as tuple (m,n) shape of matrix.

        Returns
        -------
        rows : list
            Contains list of each row.

        """
        m = self.shape[0]  # rows
        n = self.shape[1]  # columns
        rows = []  # gap for rows
        for i in range(m):  # in order to create list for each row
            row_helper = [0] * n
            for l in range(self.indptr[i], self.indptr[i + 1]):  # adjacency pairs from list indptr (Adjanzenzpaare)
                row_helper[self.indices[l]] = self.data[l]  # zeros in row_helper replaced by data
            rows = rows + [row_helper]
        return rows

    def __matmul__(self, b):
        """Matrix-vector product.

        Operator : @

        Parameters
        ----------
        A : csr_matrix
            Matrix in CSR format.
        b : list
            Vector.

        Returns
        -------
        Amatmulb : list
            Resulting vector.
        """
        A = csr_matrix.toarray(self) # firstly builds full matrix
        # now A@b
        Amatmulb = []
        x = 0
        for i in A:  # A is list, i is list in A
            j = 0
            for l in i:  # for scalars of Amatmulb
                x = x + l * b[j]  # adds up scalars
                j = j + 1
            Amatmulb = Amatmulb + [x]
            x = 0  # reset for next row
        return Amatmulb

    def __add__(self, B):
        """Sum of two matrices A and B.

        Operator : + / -

        Parameters
        ----------
        A : csr_matrix
            Contains lists of data, indices, indptr as well as tuple (m,n) shape of matrix.
        B : csr_matrix
            Contains lists of data, indices, indptr as well as tuple (m,n) shape of matrix.

        Returns
        -------
        csrAplusB : csr_matrix
            A+B in CSR format.
        """
        Aar = csr_matrix.toarray(self)
        x = len(Aar)
        Bar = csr_matrix.toarray(B)
        AplusB = []
        for i in Aar:  # i is list/ row of Aar
            k = Bar[Aar.index(i)]  # k is list/ row of Bar
            row_helper = []
            for j in range(x):
                row_helper = row_helper + [i[j] + k[j]]  # adds scalars of rows
            AplusB = AplusB + [row_helper]

       #now back to CSR format
        data = []
        indices = []
        indptr = [0]
        ptrcount = 0
        for row in AplusB:
            m = len(row)        #for shape
            for j in row:
                if j != 0:
                    data = data + [j]
                    indices = indices + [row.index(j)]
                    ptrcount = ptrcount+1
            indptr = indptr + [ptrcount]
        n = len(AplusB)
        shape = (m, n)
        csrAplusB = csr_matrix((data, indices, indptr),shape)
        return csrAplusB

