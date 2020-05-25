import numpy as np
import pandas as pd
from energyComputers.energyComputer import EnergyComputer

class CalculatedRandomEnergies(EnergyComputer):

  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.desc= "Energies randomly sampled from a weighted distribution based on the transition energies between Rydberg states\n"
    self.cache = pd.read_csv("EnergyCache.csv")
    print("hello")

  def compute_energies(self):
    probabilities = self.cache['degeneracy'] / sum(self.cache['degeneracy'])
    self.energies = np.random.choice(self.cache[' delta E in R*Z m^-1'],self.num_sites,p=probabilities)

  def get_energies(self):
    self.compute_energies()
    return self.energies 


