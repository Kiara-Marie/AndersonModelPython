import numpy as np
import pandas as pd
from energyComputers.energyComputer import EnergyComputer

class SumOnsitesDecorator(EnergyComputer):

  def __init__(self,inner_ec):
    super().__init__(inner_ec.num_sites) 
    self.inner_ec = inner_ec
    self.desc = inner_ec.desc + "Then, sum all energies, and make the actual values \
      using formula E_ij = e_ij - \sum{a,b != i,j}(e_ab)"

  def get_energies(self):
    inner_energies = self.inner_ec.get_energies() 
    summedEnergies = np.sum(inner_energies)
    actualEnergies = (inner_energies * 2) - summedEnergies
    self.energies = actualEnergies
    return self.energies 

