import numpy as np
import pandas as pd
from energyComputers.energyComputer import EnergyComputer

class CalculatedRandomEnergies(EnergyComputer):

  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.desc= "Energies randomly sampled from a weighted distribution based on the transition energies between Rydberg states\n"
    self.cache = pd.read_csv("EnergyCache.csv")
    print("hello")

  def getEnergies(self):
    probabilities = self.cache['degeneracy'] / sum(self.cache['degeneracy']);
    if self.desc == "calculated":
     self.cache_energies=np.ndarray.flatten(cache_energies) 
     self.energies = np.random.choice(self.cache_energies,self.num_sites) #input a 1D array and size, output random sampling from the array 
    
    
    return self.energies 


