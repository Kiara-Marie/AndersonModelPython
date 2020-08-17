import numpy as np
import config
from numpy.random import default_rng
from energyComputers.energyComputer import EnergyComputer

class RandomRydbergs(EnergyComputer):
  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.desc= "Each site randomly assigned pqn_0 level from uniform distribution, \
      then pqn_f level, such that pqn_0 + MIN_JUMP <= pqn_f <= pqn_0 + MAX_JUMP \
      then choosing l_0 and l_f from random uniform distribution over allowed values based on \
      the values of pqn_0 and pqn_f. Onsite energy is equal to the energy gap between the initial \
      and final state, in units of ____ \n"

    self.rng = default_rng()
    
    self.MAX_N = 100
    self.MIN_N = 1
    self.MAX_JUMP = 1
    self.MIN_JUMP = 1

    self.quantum_defects = {  
    # Quantum defect as determined by M. Bixon and J. Jortner,
    # J. Chem. Phys. 105, 1363 ~1996.
    0 : 1.21,
    1 : 0.7286,
    2 : -0.05,
    # g as determined by  Murgu, E.; Martin, J. D. D.; Gallagher, T. F..
    # The Journal of Chemical Physics 2001,115(15),7032–7040.
    3 : 0.0101,
    4 : 0}


  def get_energies(self):
    self.get_ns_and_ls(False)
    self.l0_qds = np.zeros(self.num_sites)
    self.lf_qds = np.zeros(self.num_sites)
    for i in range(4):
      self.l0_qds[self.l0s == i] = self.quantum_defects.get(i, 0)
      self.lf_qds[self.lfs == i] = self.quantum_defects.get(i, 0)
    self.energy_0s = ((self.n0s - self.l0_qds)**-2)
    self.energy_fs = ((self.nfs - self.lf_qds)**-2)
    Ry=109735.31 
    self.energies = Ry*(self.energy_fs - self.energy_0s) #Ry =0.5 in atomic unit Ry=109735.31 in cm^-1 for NO
    self.energies=self.energies*29.9792458 # convert to GHz
    return self.energies
    


  def get_ns_and_ls(self, trash):
    self.n0s = (self.MAX_N - self.MIN_N + 1) * self.rng.random(size=self.num_sites) + self.MIN_N
    np.rint(self.n0s, out=self.n0s)
    self.l0s = np.multiply(self.rng.random(size=self.num_sites),  self.n0s)
    np.rint(self.l0s, out=self.l0s)
  
    n_jumps = (self.MAX_JUMP - self.MIN_JUMP + 1) * self.rng.random(size=self.num_sites) + self.MIN_JUMP
    np.floor(n_jumps, out=n_jumps)
    self.nfs = self.n0s + n_jumps
    
    l_jumps = np.rint(self.rng.random(size=self.num_sites))
    l_jumps[l_jumps == 0] -= 1
    self.lfs = self.l0s + l_jumps