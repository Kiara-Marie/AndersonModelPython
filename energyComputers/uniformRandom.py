import numpy.random as random
class UniformRandomEnergies():

  def __init__(self, W, num_sites):
    self.W = W
    self.num_sites = num_sites

  def getEnergies(self):
    self.energies = random.uniform(-self.W/2, self.W/2, self.num_sites)
    return self.energies
