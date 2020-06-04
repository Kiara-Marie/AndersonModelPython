from abc import ABC
from jComputers.jComputer import JComputer
from class_Numerov import Numerov
 

class J_dipole(JComputer) :
  def __init__(self, nnOnly, t, rdep, energy_computer):
    """ J_ij = t , or if rdep is true, J_ij = t/r^3
    t - self-explanatory
    rdep - whether or not to have J depend on r^3
    """ 
    super().__init__(nnOnly)
    self.t = t
    self.rdep = rdep
    if (rdep):
      self.desc = "j_ij = t/r**3, with t = %f" % (t)
    else:
      self.desc = "j_ij = t, with t = %f" % (t)
    if (self.nnOnly):
      self.desc = self.desc + ", j_ij on nearest neighbours only\n" 

  def jFinder(self, xi, xj):
    if (self.nnOnly and (xi - xj) > 1):
      return 0
    r = 5*(xi - xj) 
    
    d_i=Numerov().Rad_int(n_1i,l_1i,n_2i,l_2i)
    d_j=Numerov().Rad_int(n_1j,l_1j,n_2j,l_2j)
    
    j = self.t*d_i*d_j
    if (self.rdep):
      j = j / (r*r*r)
    return j
