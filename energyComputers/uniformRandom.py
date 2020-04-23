import numpy.random as random
class UniformRandomEnergies():

  def __init__(self, W, num_sites):
    self.energies = random.uniform(-W/2, W/2, num_sites)

  def getEnergies(self):
    return self.energies