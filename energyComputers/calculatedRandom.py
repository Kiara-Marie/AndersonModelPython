import numpy as np
import pandas as pd
import config
from numpy.random import default_rng
from energyComputers.energyComputer import EnergyComputer

class CalculatedRandomEnergies(EnergyComputer):

  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.desc= "Energies randomly sampled from a weighted distribution based on the transition energies between Rydberg states\n"
    self.cache = pd.read_csv("EnergyCache.csv")
    self.rng = default_rng(config.SEED)

  def get_energies(self):
    probabilities = self.cache['degeneracy'] / sum(self.cache['degeneracy'])
    self.energies = np.random.choice(self.cache['delta E in Hz'],self.num_sites,p=probabilities)
    self.energies = self.energies/1e9  # convert to GHz
    return self.energies 


