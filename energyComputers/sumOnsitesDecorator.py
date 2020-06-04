import numpy as np
from energyComputers.energyComputer import EnergyComputer

class SumOnsitesDecorator(EnergyComputer):

  def __init__(self,inner_ec):
    super().__init__(inner_ec.num_sites) 
    self.inner_ec = inner_ec
    self.desc = inner_ec.desc + "Then, sum all energies, and make the actual values \
      using formula E_ij = e_ij - \sum{a,b != i,j}(e_ab)"

  def get_energies(self):
    self.energies = self.inner_ec.get_energies()
    summed_energies = np.sum(self.energies)
    self.actual_energies = (self.energies * 2) - summed_energies
    return self.actual_energies 
