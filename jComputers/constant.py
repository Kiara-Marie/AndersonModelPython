from abc import ABC
from jComputers.jComputer import JComputer

class Constant(JComputer) :
  def __init__(self, nnOnly, t, rdep):
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
    r = (xi - xj)
    j = self.t
    if (self.rdep):
      j = j / (r*r*r)
    return j
