import numpy as np
from energyComputers.energyComputer import EnergyComputer

class CalculatedRandomEnergies(EnergyComputer):

  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.num_sites = num_sites
    self.desc=desc
    #self.cache=cache  
    #need to constrain the formmat of cache, for example, a matrix of [n,1], or which ever coveneint to build and load 
    

  def getEnergies(self):
    #cache_energies=self.cache[:,0]
    if self.desc == "calculated":
     self.cache_energies=np.ndarray.flatten(cache_energies) 
     self.energies = np.random.choice(self.cache_energies,self.num_sites) #input a 1D array and size, output random sampling from the array 
    
    
    return self.energies 


