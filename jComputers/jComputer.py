from abc import ABC, abstractmethod

class JComputer(ABC):

  def __init__(self, nnOnly, **kwargs):
    """ JComputer init should include setting the desc string.
    This should give a brief but specific description of the method used to 
    compute off-diagonal values by this jComputer

    nnOnly is "nearest neighbours only" (i.e. for abs(i -j) != 1, J_ij = 0)
    """
    self.nnOnly = nnOnly
    self.desc = ""

  @abstractmethod
  def jFinder(self, xi, xj):
    pass

  def methodDesc(self):
    return self.desc
