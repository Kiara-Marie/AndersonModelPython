from class_Numerov import Numerov
import numpy as np
import scipy.sparse as sparse

max_n = 10
numerov = Numerov()
fid = open('tiny_cache.npz', 'wb')

num_entries = int(((max_n**2 - max_n)/2) + max_n)

rows = np.zeros(num_entries**2)
cols = np.zeros(num_entries**2)
data = np.zeros(num_entries**2)
pos = 0

for n0 in range(1, max_n):
    for l0 in range(0, n0):
        for nf in range(n0, max_n):
            for l_jump in [-1, 1]:
                lf = l0 + l_jump
                if (lf < 0 or lf >= nf):
                    continue
                dipole = numerov.Rad_int(n0, l0, nf, lf)
                rows[pos] = int((n0*(n0-1))/2 + l0)
                cols[pos] = int((nf*(nf-1))/2 + lf)
                data[pos] = dipole
                pos += 1

big_mat = sparse.coo_matrix((data, (rows, cols)), shape=(num_entries, num_entries))
sparse.save_npz(fid, big_mat)
fid.close()
