import numpy.random as random
from energyComputers.energyComputer import EnergyComputer

class UniformRandomEnergies(EnergyComputer):

  def __init__(self, W, num_sites):
    super().__init__(num_sites)
    self.W = W
    self.desc = "Onsite energies chosen from a uniform random distribution between -W/2 and W/2.\n"

  def get_energies(self):
    self.energies = random.uniform(-self.W/2, self.W/2, self.num_sites)
    return self.energies
