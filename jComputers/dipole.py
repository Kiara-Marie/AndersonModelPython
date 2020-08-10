from abc import ABC
import numpy as np
import loadFromNPZ as lfnpz
from energyComputers.sumOnsitesDecorator import SumOnsitesDecorator 
from jComputers.jComputer import JComputer

class Dipole(JComputer) :
  def __init__(self, nnOnly, t, rdep, energy_computer):
    """ j_ij = dipole as computed by Numerov/r**3 OR not divided by r**3 if no rdep
    """ 
    # avg distance from one particle to next:
    #		(10^12) particles/cm^3
    # 1/10^12 cm^3 / particle
    # 0.5/10^12 cm avg distance between them
    # so our units will be 1/10^13 cm

    super().__init__(nnOnly)
    self.t = t  # units are 1/10^13 cm 
    self.rdep = rdep
    self.energy_computer = energy_computer
    self.numerov_cache = lfnpz.load_from_npz("numerov_cache.npz")
    #self.numerov_cache = self.numerov_cache.toarray()
    if (rdep):
      self.desc = "j_ij = 	(t * dipole moment n0 * dipole moment nf) / r**3, \
      with t = %f" % (t)
    else:
      self.desc =  "j_ij = 	(t * dipole moment n0 * dipole moment nf), \
      with t = %f" % (t)
    if (self.nnOnly):
      self.desc = self.desc + "j_ij on nearest neighbours only\n" 

    if (isinstance(self.energy_computer,  SumOnsitesDecorator)):
      self.ec = self.energy_computer.inner_ec
    else:
      self.ec = self.energy_computer 

  def jFinder(self, xi, xj):
    # should only be called after this instance's energy_computer has had calculateEnergies called
    if (self.energy_computer.energies is None):
      raise Exception("Attempted to use jComputer which needs energy, but energy not yet computed!")
    if (self.nnOnly and (xi - xj) > 1):
      return 0
    r = 5*(xi - xj)
    dipole_e1 = self.get_dipole(xi)
    dipole_e2 = self.get_dipole(xj)
    j = self.t * dipole_e1 * dipole_e2
    if (self.rdep):
      j = j / (r**3)
    return j

  def get_dipole(self, x):
    n0 = self.ec.n0s[x]
    nf = self.ec.nfs[x]
    l0 = self.ec.l0s[x]
    lf = self.ec.lfs[x]
    row = int((n0*(n0-1))/2 + l0)
    col = int((nf*(nf-1))/2 + lf)
    return self.numerov_cache[row, col]