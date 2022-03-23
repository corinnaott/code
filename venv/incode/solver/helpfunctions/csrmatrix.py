class csr_matrix:
    """
    CSR (compressed sparse row): Speicherformat für Matrizen
    Instanziierung: csr_matrix((data, indices, indptr), [shape=(m,n)])

    data: Liste mit Nichtnulleinträgen
    indices: Liste mit entsprechenden Zeilenindizes für Elemente aus data
    indptr: Liste zeigt Zeilenenden der Matrix in data und indices

    shape: zweielementiges Tupel (m, n)
    m: Anzahl Zeilen
    n: Anzahl Spalten
    """

    def __init__(self, csrTuple, shape=None):
        """
        docstring!!
        :param csrTuple:
        :param shape:
        """
        _data, _indices, _indptr = csrTuple
        if shape:
            self.shape = shape
        self.data = _data
        self.indices = _indices
        self.indptr = _indptr

    def toarray(A):


        pass



        pass