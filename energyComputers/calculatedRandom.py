import numpy as np
import pandas as pd
import config
#from numpy.random import default_rng
from energyComputers.energyComputer import EnergyComputer

class CalculatedRandomEnergies(EnergyComputer):

  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.desc= "Energies randomly sampled from a weighted distribution based on the transition energies between Rydberg states\n"
    self.cache = pd.read_csv("EnergyCache.csv")
    #self.rng = default_rng(config.SEED)

  def get_energies(self):
    probabilities = self.cache['degeneracy'] / sum(self.cache['degeneracy'])
    self.index=np.random.choice(range(self.cache.shape[0]), self.num_sites,p=probabilities)
    self.energies=np.array(self.cache[' delta E in R*Z m^-1'][self.index])
    self.n1=np.array(self.cache['pqn1'][self.index])
    self.n2=np.array(self.cache[' pqn2'][self.index]) #the indent in string matters here
    self.l1=np.array(self.cache['l1'][self.index])
    self.l2=np.array(self.cache['                 l2'][self.index]) #better fix the cache
    
    #self.energies = np.random.choice(self.cache[' delta E in R*Z m^-1'],self.num_sites,p=probabilities)
    return self.energies 


