import scipy.sparse as sparse 

def load_from_npz(filename):
    f_id = open(filename, "rb")
    mat = sparse.load_npz(f_id)
    f_id.close()
    to_ret = mat.tocsr()
    return to_ret