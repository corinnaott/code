linear algebra: help functions
==============================
------------------------------

CSR matrix class
----------------

.. autoclass:: src.csrmatrix.csr_matrix
    :members: __init__ , __matmul__ , __add__  , toarray

Tridiagonal Toeplitz Matrix and Unit Matrix
--------------------------------------------

.. autofunction:: src.tridiagtoep.tridiagtoep
.. autofunction:: src.unitymatrix.I

Vectors
---------

Vector functions: build vector, dimension, scalar multiplication, addition, Euclid norm. Function for matrix-vector product.

.. autofunction:: src.linalg.vector
.. autofunction:: src.linalg.vecdim
.. autofunction:: src.linalg.scal
.. autofunction:: src.linalg.axpy
.. autofunction:: src.linalg.nrm
.. autofunction:: src.linalg.csrmv

Code
____

.. code-block:: ruby
    :linenos:
    :caption: CSR matrix class:

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

.. code-block:: ruby
    :linenos:
    :caption: Tridiagonal Toeplitz Matrix:

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


.. code-block:: ruby
    :linenos:
    :caption: Unit Matrix

    from src import csrmatrix as csr

    def I(n, delta=1):
        """
        Unit matrix I.

        Parameters
        ----------
        n : int
            Dimension of unit matrix.
        delta: int or float, optional
            Factor for scalar multiplication. The default is 1.

        Returns
        -------
        I : csr_matrix
            Unit matrix in CSR format.

        """
        I_data = []
        I_index = []
        I_indptr = [0]
        n = int(n)  # int zum iterieren

        for i in range(n):
            I_data.append(delta)
            I_index.append(i)
            I_indptr.append(i + 1)

        I = csr.csr_matrix((I_data, I_index, I_indptr), (n, n))
        return I

.. code-block:: ruby
    :linenos:
    :caption: Vectors:

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
