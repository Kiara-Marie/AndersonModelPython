import numpy as np

class CalculatedRandomEnergies():

  def __init__(self, num_sites):
      
    self.num_sites = num_sites
    #self.cache=cache  
    #need to constrain the formmat of cache, for example, a matrix of [n,1], or which ever coveneint to build and load 
    

  def getEnergies(self, cache_energies):
    #cache_energies=self.cache[:,0]
    self.cache_energies=np.ndarray.flatten(cache_energies) 
    self.energies = np.random.choice(self.cache_energies,self.num_sites) #input a 1D array and size, output random sampling from the array 
    return self.energies 


