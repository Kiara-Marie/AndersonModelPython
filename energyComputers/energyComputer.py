from abc import ABC, abstractmethod

class EnergyComputer(ABC):
  
  def __init__(self, num_sites):
    """ EnergyComputer init should include setting the desc string.
    This should give a brief but specific description of the method used to 
    compute diagonal values by this energyComputer
    """
    self.num_sites = num_sites
    self.energies = None
  
  @abstractmethod
  def get_energies(self):
    pass