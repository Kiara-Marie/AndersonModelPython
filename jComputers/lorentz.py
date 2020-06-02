from abc import ABC
import numpy as np
from jComputers.jComputer import JComputer

class Lorentz(JComputer) :
  def __init__(self, nnOnly, t, rdep, gamma, energy_computer):
    """ j_ij = lorentzian(e_i-e_j)/r**3 OR not divided by r**3 if no rdep
    """ 
    # avg distance from one particle to next:
    #		(10^12) particles/cm^3
    # 1/10^12 cm^3 / particle
    # 0.5/10^12 cm avg distance between them
    # so our units will be 1/10^13 cm

    super().__init__(nnOnly)
    self.t = t  # units are 1/10^13 cm 
    self.rdep = rdep
    self.gamma = gamma
    self.energy_computer = energy_computer
    if (rdep):
      self.desc = "j_ij = 	t/ (1 + {(e_i - e_j)/gamma^2) / r_ij**3, \
      with t = %f, gamma = %f\n" % (t, gamma)
    else:
      self.desc = "j_ij = 	t/ (1 + {(e_i - e_j)/gamma^2) \
      with t = %f, gamma = %f\n" % (t, self.gamma)
    if (self.nnOnly):
      self.desc = self.desc + "j_ij on nearest neighbours only\n" 

  def jFinder(self, xi, xj):
    # should only be called after this instance's energy_computer has had calculateEnergies called
    if (self.energy_computer.energies is None):
      raise Exception("Attempted to use jComputer which needs energy, but energy not yet computed!")
    if (self.nnOnly and (xi - xj) > 1):
      return 0
    r = 5*(xi - xj)
    denominator = 1 + ((self.energy_computer.energies[xi] - self.energy_computer.energies[xj])/(self.gamma))**2
    j = self.t / (np.pi*self.gamma * denominator)
    if (self.rdep):
      j = j / (r**3)
    return j
