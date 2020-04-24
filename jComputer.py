from abc import ABC, abstractmethod

class JComputer(ABC):

  def __init__(self, nnOnly, **kwargs):
    self.nnOnly = nnOnly
    self.desc = ""

  @abstractmethod
  def jFinder(self, xi, xj):
    pass

  def methodDesc(self):
    return self.desc
