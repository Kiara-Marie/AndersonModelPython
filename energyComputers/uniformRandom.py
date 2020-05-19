import numpy.random as random
class UniformRandomEnergies():

  def __init__(self, W, num_sites):
    self.W = W
    self.num_sites = num_sites
    self.desc = "Onsite energies chosen from a uniform random distribution between -W/2 and W/2.\n"

  def get_energies(self):
    self.energies = random.uniform(-self.W/2, self.W/2, self.num_sites)
    return self.energies
