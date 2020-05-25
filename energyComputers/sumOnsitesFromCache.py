import numpy as np
import pandas as pd
from energyComputers.calculatedRandom import CalculatedRandomEnergies

class SumOnsitesFromCache(CalculatedRandomEnergies):

  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.desc= "Energies e_ij randomly sampled from a weighted distribution \
    based on the transition energies between Rydberg states, \n \
    and then using formula E_ij = e_ij - \sum{a,b != i,j}(e_ab)"

  def get_energies(self):
    super().compute_energies()
    summedEnergies = np.sum(self.energies)
    actualEnergies = (self.energies * 2) - summedEnergies
    self.energies = actualEnergies
    return self.energies 


