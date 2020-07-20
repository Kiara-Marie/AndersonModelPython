from abc import ABC
from jComputers.jComputer import JComputer
from class_Numerov import Numerov
from energyComputers.sumOnsitesDecorator import SumOnsitesDecorator
import numpy as np

 

class J_dipole(JComputer) :
  def __init__(self, nnOnly, t, rdep, energy_computer):
    """ J_ij = t*<d_i><d_j>/r**3
    """ 
    # avg distance from one particle to next:
    #		(10^12) particles/cm^3
    # 1/10^12 cm^3 / particle
    # 0.5/10^12 cm avg distance between them
    # so our units will be 1/10^13 cm

    super().__init__(nnOnly)
    self.t = t  # Here t is just to scale the unit of dipoles. Need to be determined.
    self.rdep = rdep
    self.energy_computer = energy_computer    
    
    if (rdep):
      self.desc = "j_ij = t*<d_i><d_j>/r**3, with t = %f" % (t)
    else:
      self.desc = "j_ij = t*<d_i><d_j>, with t = %f" % (t)
    if (self.nnOnly):
      self.desc = self.desc + ", j_ij on nearest neighbours only\n"
    if (isinstance(self.energy_computer,  SumOnsitesDecorator)):
      self.ec = self.energy_computer.inner_ec
    else:
      self.ec = self.energy_computer 
    self.numerov = Numerov()

  def jFinder(self, xi, xj):
    # should only be called after this instance's energy_computer has had calculateEnergies called
    # if (self.energy_computer.energies is None):
    #   raise Exception("Attempted to use jComputer which needs energy, but energy not yet computed!")
    if (self.nnOnly and (xi - xj) > 1):
      return 0      
    r = 5*(xi - xj) 
    
    n_1i= self.ec.n0s[xi]
    l_1i= self.ec.l0s[xi]
    n_2i= self.ec.nfs[xi]
    l_2i= self.ec.lfs[xi]
    
    n_1j= self.ec.n0s[xj]
    l_1j= self.ec.l0s[xj]
    n_2j= self.ec.nfs[xj]
    l_2j= self.ec.lfs[xj]
    
    if self.energy_computer.energies[xi]*self.energy_computer.energies[xj]==0:
        j=0
    else:      
        d_i=self.numerov.Rad_int(n_1i,l_1i,n_2i,l_2i) # in atomic unit 
        d_j=self.numerov.Rad_int(n_1j,l_1j,n_2j,l_2j) # in atomic unit     
        j = self.t*d_i*d_j

    if (self.rdep):
      j = j / (r*r*r)
    return j
