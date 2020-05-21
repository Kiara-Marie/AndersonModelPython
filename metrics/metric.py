from abc import ABC, abstractmethod

class Metric(ABC):
  
  def __init__(self, num_sites, iterations):
    self.num_sites = num_sites
    self.iterations = iterations
  
  @abstractmethod
  def save(self, eigvals, eigvecs, hamiltonian):
    pass
  
  @abstractmethod
  def printResult(self, file_code):
    pass